from PIL import Image
from pathlib import Path

def savePBM(filename,x=128,y=64):
    e=Path(filename)
    if e.is_file:
        if e.suffix.upper() in [".JPG",".JPEG",".PNG",".BMP",".GIF"]:
            f=Image.open(filename)
            f=f.resize((x,y))
            l=f.convert('1')
            l.show()
            pbm=e.stem+".pbm"
            l.save(pbm,"PPM")
            print(pbm,Path(pbm).stat().st_size)
            return True
        else:
            print("请导入图片文件！")
    else:
        print("文件不存在")
    return False


savePBM("b.jpg",86,64)