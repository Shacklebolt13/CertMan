from PIL import Image, ImageDraw, ImageFont


def saveCert(
    name, template="template.jpg", Certfont="Elegante.ttf", debug=False, pdf=True
):

    template = "template.jpg"
    Certfont = "gsans.ttf"
    location = (400, 480)
    name = f"{name:^30}"
    image = Image.open(template)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(Certfont, size=70)
    color = "rgb(0, 230, 118)"

    draw.text(location, name, fill=color, font=font)
    imageName = "certs/" + name.strip()

    if pdf == True:
        image.convert("RGB")
        imageName += ".pdf"
        image.save(imageName)
    else:
        imageName += ".jpg"
        image.save(imageName)

    if debug == True:
        print("name:", name, "location:", location, "saved at:", imageName)

    return imageName


saveCert("Test", pdf=False)
