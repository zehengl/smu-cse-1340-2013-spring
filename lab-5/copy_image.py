path_source = pickAFile()
pic_source = makePicture(path_source)
h_source = getHeight(pic_source)
w_source = getWidth(pic_source)

path_target = pickAFile()
pic_target = makePicture(path_target)
h_target = getHeight(pic_target)
w_target = getWidth(pic_target)

for x in range(0, w_source):
    for y in range(0, h_source):
        pix_source = getPixel(
            pic_source,
            x,
            y,
        )
        pix_top_left = getPixel(
            pic_target,
            x,
            y,
        )
        pix_top_right = getPixel(
            pic_target,
            w_target - w_source + x,
            y,
        )
        pix_bottom_left = getPixel(
            pic_target,
            x,
            h_target - h_source + y,
        )
        pix_bottom_right = getPixel(
            pic_target,
            w_target - w_source + x,
            h_target - h_source + y,
        )

        setColor(
            pix_top_left,
            makeColor(getRed(pix_source), getGreen(pix_source), getBlue(pix_source)),
        )
        setColor(
            pix_top_right,
            makeColor(getRed(pix_source), getGreen(pix_source), getBlue(pix_source)),
        )
        setColor(
            pix_bottom_left,
            makeColor(getRed(pix_source), getGreen(pix_source), getBlue(pix_source)),
        )
        setColor(
            pix_bottom_right,
            makeColor(getRed(pix_source), getGreen(pix_source), getBlue(pix_source)),
        )


show(pic_target)
