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

# Video_compression_new
代码说明：
依赖要求：需要提前安装FFmpeg（可通过包管理器或官网下载）
参数说明：
resolution：字符串格式（如"1280x720"），支持以下常见分辨率：
4K: 3840x2160
2K: 2560x1440
1080p: 1920x1080
720p: 1280x720
480p: 640x480
压缩选项：
-crf 23：视频质量参数（18-28，数值越小质量越高）
-preset medium：编码速度预设（更快的编码速度会降低压缩效率）
-c:a copy：直接复制音频流（不重新编码）
使用方法：
将代码保存为video_compressor.py
在命令行运行：
bash
python video_compressor.py
修改input_file和output_file路径，调整target_resolution参数
注意事项：
如果遇到FFmpeg错误，请确保：
FFmpeg已正确安装
输入文件路径正确
输出目录有写入权限
对于大文件压缩，建议使用-preset slower提高压缩率（但会增加处理时间）
