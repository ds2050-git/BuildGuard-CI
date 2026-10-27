import subprocess
import json
import os
import time

def mk_log():
    fn="test_results.log"
    d=["TEST_1:PASS","TEST_2:PASS","TEST_3:FAIL","TEST_4:PASS"]
    with open(fn,"w") as f:
        f.write("\n".join(d)+"\n")
    return fn

def comp():
    subprocess.run(["g++","-std=c++17","validator_core.cpp","-o","validator_core"],check=True)

def run():
    if not os.path.exists("validator_core"):comp()
    lf=mk_log()
    res=subprocess.run(["./validator_core",lf],capture_output=True,text=True)
    rep={"timestamp":int(time.time()),"status":"completed","output":res.stdout.strip()}
    print(json.dumps(rep,indent=2))

if __name__=="__main__":
    run()