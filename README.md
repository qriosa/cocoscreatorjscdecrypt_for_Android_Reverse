# cocoscreatorjscdecrypt_for_Android_Reverse
[TOC]

## ZH

### 背景

本工具只是 fork 了 [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt)， 然后进行了简单的修改。使得在对APK文件进行逆向分析过程中，对其中的 `.jsc` 进行解密的使用方法变得更加简单便捷。

原工具的 readme 如下：

> cocoscreator 官方在编译的时候只给了加密的方法，而生成jsc之后没有进行解密的，这里给出一个开箱即用的方法。
>
> 1. 安装nodejs
> 2. npm install xxtea-node
>    npm install pako
> 3. 修改 cocoscreator加密时候的KEY，是否压缩UNZIP，jsc所在的目录（会递归所有子目录，jsc文件后缀进行解密）
> 4. 执行 node decrypt.js 即可获得



### 使用

1. 安装 `python3` 和 `node.js` 。
2. 下载此项目压缩包并解压。
3. 在当前项目文件夹下执行命令 `npm install xxtea-node npm install pako` 。
4. 运行命令 `python decodejsc.py APK_filepath/xxx.apk` 。

运行完毕，程序会将 `xxx.apk` 解压到 `APK_filepath` 然后将其中所有的 `yyy.jsc` 文件解密并保存到与原密文文件 `yyy.jsc` 相同目录下，命名为 `yyy.jsc.js` 。



### License

本工具本身遵守 `MIT` license，但由于主体功能 fork 自 [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt) ，因此还因遵守 [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt) 的 [license](https://github.com/luckyaibin/cocoscreatorjscdecrypt/blob/master/LICENSE)。



## EN

### Background

This tool is just forked from [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt), and then made a simple modification. It makes it easier to decrypt the `.jsc` in APK files during Android reverse analysis.

The readme of the original tool is as follows.

> cocoscreator 官方在编译的时候只给了加密的方法，而生成jsc之后没有进行解密的，这里给出一个开箱即用的方法。
>
> 1. 安装nodejs
> 2. npm install xxtea-node
>    npm install pako
> 3. 修改 cocoscreator加密时候的KEY，是否压缩UNZIP，jsc所在的目录（会递归所有子目录，jsc文件后缀进行解密）
> 4. 执行 node decrypt.js 即可获得



### Useage

1. Install `python3` and `node.js`.
2. Download the project zip file and unzip it. 
3. Run the command `npm install xxtea-node npm install pako` in the current project folder. 
4. Run the command `python decodejsc.py APK_filepath/xxx.apk` .

After running, the program will decompress `xxx.apk` to `APK_filepath` and then decrypt all the `yyy.jsc` files in it and save them to the same directory as the original cipher file `yyy.jsc`, named `yyy.jsc.js`.



### License

The tool itself adheres to the `MIT` license, but since the main function is forked from [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt), it also adheres to the [license](https://github.com/luckyaibin/cocoscreatorjscdecrypt/blob/master/LICENSE) of [cocscreatorjscdecrypt](https://github.com/luckyaibin/cocoscreatorjscdecrypt).
