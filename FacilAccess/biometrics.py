from PIL import Image, ImageDraw
import pygame


class FaceDetector:
    def __init__(self):
        self.face_template = Image.open(
            "assets/ui/face_template.png")  # Template de referência

    def detect_face(self, image_path):
        """Usa Pillow para comparar features faciais com o template"""
        user_image = Image.open(image_path)
        # Lógica simplificada de detecção (pode ser adaptada)
        return self._compare_images(user_image, self.face_template)

    def _compare_images(self, img1, img2):
        """Comparação baseada em histograma de cores"""
        hist1 = img1.histogram()
        hist2 = img2.histogram()
        # Threshold
        return sum((a - b) ** 2 for a, b in zip(hist1, hist2)) ** 0.5 < 50
