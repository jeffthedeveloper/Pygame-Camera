# FacilAccess: Sistema de Biometria Simulado com Pygame

`FacilAccess` é um projeto em Python que utiliza `Pygame` para a interface gráfica e `Pillow` (PIL) para simular um sistema de reconhecimento facial e análise de emoções.

Este projeto serve como uma prova de conceito para um loop de aplicação que integra captura de imagem (simulada) com lógica de processamento de imagem básica, demonstrando a interação entre diferentes módulos em uma aplicação de desktop.

## Tecnologias Utilizadas

  * **Python 3**
  * **Pygame:** Utilizado para criar a janela da aplicação, gerenciar o loop de eventos e exibir a interface.
  * **Pillow (PIL):** Utilizada no módulo de biometria para processamento de imagem, especificamente para carregar imagens e comparar histogramas.

## Funcionalidades e Conceito

O fluxo principal da aplicação é gerenciado pelo `main.py`, que inicializa o Pygame e entra em um loop de renderização.

### Biometria Simulada (`biometrics.py`)

A detecção facial neste projeto **é uma simulação** e não utiliza inteligência artificial ou machine learning. A lógica está contida na classe `FaceDetector`:

1.  Um template de rosto (`assets/ui/face_template.png`) é carregado na inicialização.
2.  A função `detect_face` recebe o caminho de uma imagem do usuário (atualmente um placeholder: `"temp_capture.png"`).
3.  O método `_compare_images` compara o histograma de cores da imagem do usuário com o histograma do template.
4.  Se a diferença entre os histogramas estiver abaixo de um limite (threshold), a função retorna `True` (rosto "detectado").

### Status dos Módulos

  * **`main.py`**: Funcional, com loop principal e placeholders.
  * **`core/biometrics.py`**: Funcional (simulação baseada em histograma).
  * **Análise de Emoção**: Atualmente é um placeholder. O `main.py` define um valor estático (`emotion = "Happy"`), indicando onde a lógica de análise de sentimentos (definida no `README.md` do projeto como `emotion_analyzer.py`) seria integrada.
  * **Captura de Câmera**: Não implementada. O sistema depende de um arquivo de imagem estático (`temp_capture.png`).

## Estrutura do Projeto

A estrutura de diretórios planejada para o projeto é a seguinte (baseada no `README.md` do repositório):

```
FacilAccess/
├── main.py                      # Ponto de entrada (Pygame loop)
├── core/
│   ├── biometrics.py            # Biometria via Pillow (detecção de rostos/features)
│   ├── emotion_analyzer.py      # (Planejado) Análise de sentimentos
│   └── database.py              # (Planejado) Armazenamento local
├── assets/
│   ├── ui/
│   │   ├── face_template.png    # Imagem de referência para biometria
│   │   ├── menu.png
│   │   ├── camera.png
│   │   └── emotions/
│   └── fonts/
├── config/
│   └── settings.py              # (Planejado) Configurações
└── README.md
```

## Como Executar o Projeto

1.  **Pré-requisitos:**

      * Python 3.x
      * Pip (gerenciador de pacotes)

2.  **Clone o Repositório:**

    ```bash
    git clone <url-do-repositorio>
    cd Pygame-Camera-f7ecd9115ed668be271368e133661434219e1b20/FacilAccess
    ```

3.  **Crie um Ambiente Virtual (Recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

4.  **Instale as Dependências:**
    O projeto requer `pygame` e `pillow`.

    ```bash
    pip install pygame pillow
    ```

5.  **Prepare os Assets (Placeholders):**
    O código espera encontrar dois arquivos para funcionar:

      * `assets/ui/face_template.png`: Crie esta pasta e coloque uma imagem de rosto de referência.
      * `temp_capture.png`: Coloque uma imagem de "captura" na raiz (`FacilAccess/`). *Para testar a detecção, esta imagem deve ser similar à `face_template.png`.*

6.  **Execute a Aplicação:**

    ```bash
    python main.py
    ```
