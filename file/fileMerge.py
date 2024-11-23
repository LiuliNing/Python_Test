import os
import shutil


# 进行检查
def is_subdirectory(parent, child):
    """ 检查child是否是parent的子目录 """
    parent = os.path.abspath(parent)
    child = os.path.abspath(child)
    return os.path.commonpath([parent]) == os.path.commonpath([parent, child])


# 合并目录
def merge_files(source_dir, target_dir, delete_source=False):
    """
    执行命令，将所有读到的数据去除空行
    :param source_dir: 原目录
    :param target_dir: 目标目录
    :param delete_source: 是否删除源文件，默认不删除
    :return: 去除空行后的命令
    """
    # 检查目标目录是否是源目录的子目录
    if is_subdirectory(source_dir, target_dir):
        print("Error: Target directory is a subdirectory of the source directory.")
        return

    # 确保目标文件夹存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源文件夹及子文件夹
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 构建原始文件路径
            source_path = os.path.join(root, file)
            # 构建目标文件路径
            target_path = os.path.join(target_dir, file)

            # 检查文件是否已存在于目标文件夹中
            if not os.path.exists(target_path):
                # 复制文件到目标文件夹
                shutil.copy2(source_path, target_path)  # 使用copy2保持元数据
                print(f"Copied: {source_path} to {target_path}")

                # 如果设置了删除源文件的选项，则删除源文件
                if delete_source:
                    os.remove(source_path)
                    print(f"Deleted: {source_path}")
            else:
                print(f"Skipped: {file} already exists in {target_dir}")


# 调用函数
if __name__ == '__main__':
    # 指定源目录和目标目录
    source_directory = r'F:\待整理'
    target_directory = r'F:\to'
    merge_files(source_directory, target_directory, False)
