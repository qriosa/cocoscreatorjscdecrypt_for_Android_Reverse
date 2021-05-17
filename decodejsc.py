from subprocess import Popen
import sys
import zipfile
import os
import shutil

def get(filename = "libcocos2djs.so"):
    with open(filename, "rb") as f:
        content = f.read()
    start = content.find(b"Cocos Game") + 10 # 直接从Game后面开始查

    if start < 0 or start > len(content):
    	return ""

    for i in range(start, len(content)):
        if content[i] > 32 and content[i] < 128:
            start = i
            break

    key = ""
    for i in range(start, len(content)):
        if content[i] < 33 or content[i] > 127:
            break
        key += chr(content[i])
    return key

def getKEY(FILEPATH):
	dirs = os.listdir(os.path.join(FILEPATH, "lib")) # ['arm64-v8a', 'armeabi', 'armeabi-v7a', 'mips', 'mips64', 'x86', 'x86_64']
	# 遍历各个平台架构 寻找第一个 libcocos2djs.so
	for dirname in dirs:
		dirpath = os.path.join(FILEPATH, "lib", dirname)
		if not os.path.isdir(dirpath):
			continue
		files = os.listdir(dirpath) # ['libads-c.so', 'libcocos2djs.so', 'libnms.so', 'libpl_droidsonroids_gif.so', 'libtobEmbedEncrypt.so']
		if "libcocos2djs.so" in files:
			return get(os.path.join(dirpath, "libcocos2djs.so"))

	# 如果不存在 libcocos2djs.so 那么就开始暴力枚举
	for dirname in dirs:
		dirpath = os.path.join(FILEPATH, "lib", dirname)
		if not os.path.isdir(dirpath):
			continue		
		files = os.listdir(dirpath) # ['libads-c.so', 'libcocos2djs.so', 'libnms.so', 'libpl_droidsonroids_gif.so', 'libtobEmbedEncrypt.so']
		for filename in files:
			key = get(os.path.join(dirpath, filename))
			if not key:
				return key


def show_help():
	print("""
usage:
[ZH]
	python decodejsc.py APK_path [UNZIP]

	APK_path :	字符串,
				你想解密 '.jsc' 文件的 APK 文件的路径。
	UNZIP    :	[0, 1]，
				在解密过程中是否启用压缩。

[EN]
	python decodejsc.py APK_path [UNZIP]

	APK_path :	strings,
				the file path of the APK that has '.jsc' file you want to decode.
	UNZIP    : [0, 1], 
				using unzip or not during decoding.

""")
	sys.exit()

if __name__ == '__main__':
	try:
		if len(sys.argv) == 2:
			APK_path = os.path.join(sys.argv[1])
			UNZIP = 1
		elif len(sys.argv) == 3:
			APK_path = os.path.join(sys.argv[1])
			UNZIP = 1 if str(sys.argv[2]) == "1" else 0
		else:
			show_help()
	except:
		show_help()

	FILEPATH = os.path.splitext(APK_path)[0]

	print("正在解压中(Decompressing)...")
	# 解压文件
	with zipfile.ZipFile(APK_path, 'r') as zip_ref:
		zip_ref.extractall(FILEPATH)

	print("正在获取 KEY (Getting KEY)...")
	# 获取 KEY
	KEY = getKEY(FILEPATH)

	print("正在解密中 (decrypting)...\n")
	cmd = ['node', 'decode.js', f'FILEPATH={FILEPATH}', f'KEY={KEY}', 'UNZIP=1']
	
	p = Popen(cmd)
	(output, err) = p.communicate()
	#This makes the wait possible
	p_status = p.wait()

	#This will give you the output of the command being executed
	# print( "Command output: " + str(output))
	print("\n解密完成(Decryption completed)!")

	# 删除刚刚解压的文件
	# shutil.rmtree()
