from pathlib import Path
import os
import subprocess
import time

root = Path(__file__).resolve().parents[1]
exe = root/'build/windows-package/Green-Ball-Windows/GreenBall/GreenBall.exe'
env = dict(os.environ, SDL_VIDEODRIVER='dummy', SDL_AUDIODRIVER='dummy')
with open(root/'build/game-start.log', 'w') as log:
    p = subprocess.Popen([str(exe)], cwd=exe.parent.parent, env=env, stdout=log, stderr=log)
    try:
        time.sleep(8)
        assert p.poll() is None, 'Le jeu s’est ferme au demarrage : voir build/game-start.log'
    finally:
        if p.poll() is None:
            p.terminate()
        p.wait(timeout=10)
print('OK : le jeu empaquete demarre avec ses ressources et reste actif.')
