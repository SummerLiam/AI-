from PIL import Image, ImageDraw

def create_character(hair_color, eye_color, clothes_color, gender):

    img = Image.new("RGBA",(32,32),(0,0,0,0))
    draw = ImageDraw.Draw(img)

    skin = (255,220,177)

    if gender == "female":
        draw.rectangle([8,2,23,12], fill=hair_color)
    else:
        draw.rectangle([9,2,22,7], fill=hair_color)

    draw.rectangle([10,4,21,15], fill=skin)

    draw.point((13,9), fill=eye_color)
    draw.point((18,9), fill=eye_color)

    draw.rectangle([10,16,21,24], fill=clothes_color)

    draw.rectangle([8,16,9,23], fill=skin)
    draw.rectangle([22,16,23,23], fill=skin)

    draw.rectangle([11,25,14,30], fill=(40,40,160))
    draw.rectangle([17,25,20,30], fill=(40,40,160))

    draw.rectangle([10,30,14,31], fill=(80,80,80))
    draw.rectangle([17,30,21,31], fill=(80,80,80))

    return img