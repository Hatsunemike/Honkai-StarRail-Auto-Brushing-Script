import pyautogui as pygui
from PIL import Image
import cv2
import numpy as np
import time

def ToCv2MatLike(image: Image.Image) -> cv2.typing.MatLike:
    if image.mode == "BGR":
        return np.array(image)
    elif image.mode == "RGB":
        return cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

FindThreshold = 0.1 # Threshold of Find
def Find(target: cv2.typing.MatLike, template: cv2.typing.MatLike, debug: bool = False) -> tuple:
    # Use template-match to check if picture "Template" is in picture "Target"
    # If it's not in, return a bool-varient False;
    # if it's in, return a tunple (True, min_loc:Point, tmp_h, tmp_w)
    tmp_h, tmp_w = template.shape[:2]
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # find the most-matching location and it's matching-value
    if debug == True: 
        #匹配值转换为字符串
        #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
        #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
        strmin_val = str(min_val)
        #绘制矩形边框，将匹配区域标注出来
        #min_loc：矩形定点
        #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
        #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
        cv2.rectangle(target,min_loc,(min_loc[0]+tmp_w,min_loc[1]+tmp_h),(0,0,225),2)
        #显示结果,并将匹配值显示在标题栏上
        cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
        cv2.waitKey()
        cv2.destroyAllWindows()
    if min_val <= FindThreshold:
        return (True, min_loc, tmp_h, tmp_w)
    else :
        return (False,False)

def ClickButton(im_button: cv2.typing.MatLike|str) :
    # given a button image, find it on screen and then click it.
    if isinstance(im_button,str):
        im_button = cv2.imread(im_button)
    while(1) :
        screenshot = ToCv2MatLike(pygui.screenshot()) # type : cv2.typing.MatLike
        find_tuple = Find(screenshot, im_button)
        if(find_tuple[0] == True) :
            find_result, min_loc, tmp_h, tmp_w = find_tuple
            break
    click_w = min_loc[0]+tmp_w/2
    click_h = min_loc[1]+tmp_h/2
    pygui.leftClick(click_w,click_h,duration=0.1)

if __name__ == "__main__" :
    completeOnceImage = cv2.imread("./CompleteOnce.png") # type: cv2.typing.matlike
    supplementImage = cv2.imread("./Supplement.png")
    reservedTrailblazePowerImage = cv2.imread("./ReservedTrailblazePower.png")
    while(1) :
        screenshot = ToCv2MatLike(pygui.screenshot()) # type : cv2.typing.MatLike
        if Find(screenshot, completeOnceImage)[0] == True :
            print("检测到：完成一次刷本")
            time.sleep(1)
            ClickButton("Again.png")
        elif Find(screenshot, supplementImage)[0] == True :
            print("检测到需要补充开拓力")
            if(Find(screenshot, reservedTrailblazePowerImage)[0] == True) :
                ClickButton("Confirm.png")
                time.sleep(1)
                ClickButton("InputBox.png")
                time.sleep(1)
                pygui.typewrite("40",interval=0.25)
                time.sleep(1)
                ClickButton("Confirm.png")
                time.sleep(1)
                pygui.click()
                time.sleep(1)
                ClickButton("Again.png")