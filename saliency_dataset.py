class SaliencyInstance(datasets.ImageFolder):

    def __getitem__(self, index):
        # load the image and its corresponding saliency
        ipath, _ = self.imgs[index]
        img = self.loader(ipath)
        spath, _ = self.saliencies[index]
        saliency = self.loader(spath)
        
        if self.transform is not None:
            # copy-paste augmentation
            img = self.composite_background(image, saliency)
            # other augmentation follows
            img = self.transform(img)
        else:
            img = image

        if self.two_crop:
            img2 = self.composite_background(image, saliency)
            img2 = self.transform(img2)
            img = torch.cat([img, img2], dim=0)

        return img, index

    def composite_background(self, img, saliency):

        # probablity = 0.7 to return the original image
        if random.random() < 0.7:
            return img

        # otherwise, paste the foreground to a random background
        background = np.empty((224,224,3), dtype=np.uint8)
        background[:] = math.floor(random.random() * 255)
        background = Image.fromarray(background)

        # adjust the size of the background to img
        w,h = img.size
        bw,bh = background.size
        ratio = 1.
        if bw < w and bh < h:
            ratio = max(w/bw,h/bh)
        elif bw < w and bh >= h:
            ratio = w / bw
        elif bw >= w and bh < h:
            ratio = h / bh
        bw, bh = int(bw * ratio), int(bh * ratio)
        background = background.resize((bw,bh), Image.BILINEAR)

        # crop the desired size
        crop_top = int(round((bh - h) / 2.))
        crop_left = int(round((bw - w) / 2.))
        crop_top = random.randint(0, crop_top)
        crop_left = random.randint(0, crop_left)
        background = background.crop((crop_left, crop_top,
            crop_left+w, crop_top+h))

        # Blending the saliency map with a probability 0.5
        if random.random() < 0.5:
            saliency = saliency.filter(ImageFilter.GaussianBlur(5))

        # composite the final image
        img = Image.composite(img, background, saliency)

        return img