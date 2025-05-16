✅ Estrutura do Projeto

FaceEmotionPygame/
├── main.py                      # Ponto de entrada (Pygame loop)
├── core/
│   ├── biometrics.py            # Biometria via Pillow (detecção de rostos/features)
│   ├── emotion_analyzer.py      # Análise de sentimentos (baseada em cores/expressões)
│   └── database.py              # Armazenamento local (SQLite ou JSON)
├── assets/
│   ├── ui/                      # Telas do Pygame
│   │   ├── menu.png             # Placeholder - tela inicial
│   │   ├── camera.png           # Placeholder - fundo da câmera
│   │   └── emotions/            # Ícones de emoções (feliz, triste, etc.)
│   └── fonts/                   # Fontes para UI
├── config/
│   └── settings.py              # Cores, resolução, paths
└── README.md                    # Docs em inglês


