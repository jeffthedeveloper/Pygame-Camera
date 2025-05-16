import pygame
from core.biometrics import FaceDetector


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    detector = FaceDetector()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Exemplo: captura de imagem e análise
        user_face = "temp_capture.png"
        if detector.detect_face(user_face):
            emotion = "Happy"  # Placeholder para análise de sentimentos
            pygame.display.set_caption(f"Emoção detectada: {emotion}")

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
