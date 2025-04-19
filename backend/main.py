from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pedalboard import (
    Pedalboard,
    Reverb,
    Delay,
    Distortion,
    Chorus,
    LadderFilter,
    Phaser,
    Gain,
)
from pedalboard.io import AudioFile
import os
import time
import uuid
import glob


def cleanup_temp_files(older_than_secs=3600):
    now = time.time()
    for f in glob.glob("temp/*.wav"):
        if os.path.isfile(f) and (now - os.path.getmtime(f)) > older_than_secs:
            os.remove(f)


app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

os.makedirs("temp", exist_ok=True)


@app.get("/")
def serve_homepage():
    return HTMLResponse(open("frontend/index.html").read())


@app.get("/map")
def stage_map():
    return HTMLResponse(open("frontend/stage-map.html").read())


@app.get("/stage1-distortion")
def stage1():
    return HTMLResponse(open("frontend/stage1-distortion.html").read())


@app.get("/stage2-chorus")
def stage2():
    return HTMLResponse(open("frontend/stage2-chorus.html").read())


@app.get("/stage3-reverb")
def stage3():
    return HTMLResponse(open("frontend/stage3-reverb.html").read())


@app.get("/stage4-delay")
def stage4():
    return HTMLResponse(open("frontend/stage4-delay.html").read())


@app.get("/stage5-boss")
def stage5():
    return HTMLResponse(open("frontend/stage5-boss.html").read())


@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...), effect: str = Form(...)):

    cleanup_temp_files(older_than_secs=3600)

    uid = str(uuid.uuid4())
    input_path = f"temp/{uid}.wav"
    output_path = f"temp/{uid}_processed.wav"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    with AudioFile(input_path) as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    # Choose effect
    if effect == "reverb":
        board = Pedalboard([Reverb(room_size=1)])
    elif effect == "chorus":
        board = Pedalboard([Chorus(depth=1.0)])
    elif effect == "delay":
        board = Pedalboard([Delay(delay_seconds=0.5, feedback=0.5)])
    elif effect == "distortion":
        board = Pedalboard([Distortion(drive_db=15)])
    else:
        board = Pedalboard(
            [
                Gain(gain_db=10),
                Distortion(drive_db=10),
                Chorus(depth=1.0),
                LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=900),
                Phaser(),
                Reverb(room_size=0.75),
                Delay(delay_seconds=0.5),
            ]
        )

    effected = board(audio, samplerate)

    with AudioFile(output_path, "w", samplerate, effected.shape[0]) as f:
        f.write(effected)

    return FileResponse(output_path, media_type="audio/wav", filename="processed.wav")
