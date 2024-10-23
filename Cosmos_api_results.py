## https://cosmos-rpc.publicnode.com:443
import os
import subprocess
import random
import time

dir_path = "../blockdata/Cosmos_Hub/block_results"
files = os.listdir(dir_path)
print(len(files))
print(type(files))
print("MAX",max(files))
height = int(max(files)[:-5])
# height = int(22250000)#22320310
check_range = int(100000)

def save_file(output_file, url):
    # ファイルを開く
    with open(output_file, 'w') as file:
        # curlコマンドを実行し、出力をファイルにリダイレクト
        result = subprocess.run(['curl', '-s', url], stdout=file, stderr=subprocess.PIPE, text=True)

    # エラーがあれば表示
    if result.stderr:
        print("Error:\n", result.stderr)

    # コマンドの終了コードを表示
    print("Return Code:", result.returncode)

# def 

for i in range(check_range):
    print(height)
    url1 = "https://cosmos-rpc.publicnode.com/block_results?height=" + str(height)
    output_file ="/media/admin-f/WD_BLACK/blockdata/Cosmos_Hub/block_results_1023/" + str(height) + ".json"
    save_file(output_file, url1)
    t = random.randint(1,3)
    print("sleep time is",t)
    time.sleep(t)
    ##
    url2 = "https://cosmos-rpc.publicnode.com/block?height=" + str(height)
    output_file ="/media/admin-f/WD_BLACK/blockdata/Cosmos_Hub/block_header/" + str(height) + ".json"
    save_file(output_file, url2)
    t = random.randint(1,3)
    print("sleep time is",t)
    time.sleep(t)
    height += 1
