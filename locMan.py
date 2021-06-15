from PIL import Image, ImageDraw, ImageFont


def saveCert(name,template='template.jpg',Certfont='Elegante.ttf',debug=False,pdf=True):
    
    template='template.jpg'
    Certfont='Elegante.ttf'
    location=(220,430)

    image = Image.open(template)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(Certfont, size=70)
    color = 'rgb(0, 0, 0)'
    
    
    
    draw.text(location, name, fill=color, font=font)
    imageName = "certs/"+name
    
    if(pdf==True):     
        image.convert('RGB')
        imageName+=".pdf"
        image.save(imageName)
    else:
        imageName+=".jpg"
        image.save(imageName)
    
    if(debug==True):
        print("name:",name,"location:",location,"saved at:",imageName)
    
    return imageName

saveCert("Test")