# Video_compression
使用说明
依赖安装:

需要安装FFmpeg并添加到系统PATH

安装Python依赖: pip install pathlib

参数说明:

crf: 控制压缩质量(0-51)，数值越大压缩率越高，质量越低。推荐值18-28

preset: 控制编码速度与压缩率的平衡，从快到慢有: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow

target_size: 可选，指定目标文件大小(MB)

使用方法:

将需要压缩的视频放入input_videos文件夹

运行脚本，压缩后的视频将输出到compressed_videos文件夹

可以根据需要修改crf值或使用target_size参数

注意事项
此脚本使用H.264编码器，兼容性较好

音频使用AAC编码，固定128kbps比特率

对于非常大的压缩比例，视频质量会明显下降

确保有足够的磁盘空间用于临时文件

如果需要更高级的功能，可以考虑添加分辨率缩放、帧率调整等选项。
