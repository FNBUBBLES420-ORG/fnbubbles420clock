# 🕒 FNBUBBLES420 ORG - Official Clock 🕒

Welcome to the official repository for the FNBUBBLES420 ORG Clock, a sleek and modern clock interface built with Pygame. This application provides real-time updates of the current time and date 📅, set against a dynamic gradient background that shifts colors 🌈 to enhance visual appeal. ✨


## Key Features

- **Real-time Clock**: Displays the current time and date, updating every second.
- **Dynamic Background**: Features a color-changing gradient background that updates every minute.
- **Resource-Efficient**: Optimized to ensure minimal CPU usage while running continuously.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Before you begin, ensure you have the following software installed:
- Python 3.11.6 (Download from [Python 3.11.6](https://github.com/fnbubbles420-org/Py3.11.6installer)
- Pygame Library (`pip install pygame`)

### Installation

1. Clone the repository or download the ZIP package:
```
git clone https://github.com/fnbubbles420-org/fnbubbles420clock.git
```

2. Navigate to the project directory:

```
cd fnbubbles420clock
```

### Before running the application, you will need to install the required Python libraries. After cloning the repository, navigate to the project directory and run:

```
pip install -r requirements.txt
```


3. Run the application:

```
python main.py
```

---
---
## Screenshot
![clock](https://github.com/FNBUBBLES420-ORG/fnbubbles420clock/blob/main/clock.png)
---
---

# FNBUBBLES420 ORG - Official Clock Executable

Welcome to the official distribution page for the FNBUBBLES420 ORG Clock, a desktop application that provides a dynamic digital clock with aesthetic appeal. This executable allows you to run the application without the need for manual installation steps.

## Installation

Download the executable from the official [Releases page](https://github.com/FNBUBBLES420-ORG/fnbubbles420clock/releases/tag/fnbubbles420clock-exe). Save the executable to your preferred location on your computer.

## Running the Application

Double-click the executable file to launch the clock. The application will display the current time with a visually pleasing background that changes over time.

## Verifying the Digital Signature

To ensure the integrity and authenticity of the executable, follow these steps to verify its digital signature:

1. **Right-click** on the executable file.
2. Select **Properties**.
3. Go to the **Digital Signatures** tab.
   - Click the timestamp date **Saturday**.
4. Click on **Details**.
   - Click **View Certificate**.
5. Click **Install Certificate**.
   - Choose **Current User** and click **Next**.
6. Select **Place All Certificates in the Following Store**.
   - Click **Browse**.
7. Choose **Trusted Root Certification Authorities**.
   - Click **OK**.
8. The certificate will be imported after you click **Finish**.
   - Click **Finish**.
9. Repeat step 3. Go back to the **Digital Signatures** tab.
   - Click the timestamp date **Saturday**.
   - A warning message may pop up; click **Yes**.
10. Verify if the **Signature** is valid.
    - Ensure that the digital signature is reported as "OK".

Following these steps will help confirm that the executable has not been tampered with and is safe to run.

## Troubleshooting

Should you encounter any issues with running the executable or if security warnings appear, ensure that the digital signature has been properly verified. If problems persist, please refer to the support contact information below.

# LICENSE
## ***This project is proprietary and all rights are reserved by the author.***
## ***Unauthorized copying, distribution, or modification of this project is strictly prohibited.***
## ***Unless You have written permission from the Developer or the FNBUBBLES420 ORG.***


## Contact

For support or additional information, [Join the Discord](https://discord.fnbubbles420.org/invite).

Thank you for using the FNBUBBLES420 ORG Clock. We hope you find it both useful and enjoyable!

---
---

# Acknowledgements
- [jpb1991](https://github.com/jpb1991) providing the example code then i enhanced it
- this is his code below:
```python
import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 250
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Local Time Clock")

# Define colors
background_color = (240, 240, 240)  # Light gray background
text_color = (0, 0, 0)  # Black text
shadow_color = (50, 50, 50)  # Gray shadow for text

# Load a system font
font = pygame.font.SysFont('segoeui', 72)  # You can change 'segoeui' to 'arial' if needed

# Clock for refreshing the screen
clock = pygame.time.Clock()

def draw_text_with_shadow(surface, text, font, text_color, shadow_color, position):
    text_surface = font.render(text, True, text_color)
    shadow_surface = font.render(text, True, shadow_color)
    text_rect = text_surface.get_rect(center=position)
    shadow_rect = shadow_surface.get_rect(center=(position[0] + 2, position[1] + 2))
    surface.blit(shadow_surface, shadow_rect)
    surface.blit(text_surface, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current local time and date
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %d %B %Y")

    # Draw background, time, and date with shadows
    screen.fill(background_color)
    draw_text_with_shadow(screen, current_time, font, text_color, shadow_color, (width // 2, height // 2 - 30))
    draw_text_with_shadow(screen, current_date, font, text_color, shadow_color, (width // 2, height // 2 + 40))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to limit updates to once per second
    clock.tick(1)
```
