#!/usr/bin/env bash

# Кольори для гарного оформлення терміналу
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

BINARY_NAME="jppi"
TARGET_DIR="$HOME/.jpp"

echo -e "${PURPLE}=======================================${NC}"
echo -e "${PURPLE}    Java++ (JPP) Installer Runtime     ${NC}"
echo -e "${PURPLE}=======================================${NC}"

# 1. Перевірка наявності бінарника в поточній папці
if [ ! -f "./$BINARY_NAME" ]; then
    echo -e "${RED}Error: '$BINARY_NAME' binary not found in the current directory!${NC}"
    exit 1
fi

# 2. Створення цільової папки в домашній директорії
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
    echo -e "${CYAN}Created target directory: $TARGET_DIR${NC}"
fi

# 3. Копіювання та видача прав на виконання
cp "./$BINARY_NAME" "$TARGET_DIR/"
chmod +x "$TARGET_DIR/$BINARY_NAME"
echo -e "${GREEN}Successfully copied and set executable permissions for $BINARY_NAME!${NC}"

# 4. Визначення конфігураційного файлу оболонки
SHELL_RC=""
if [[ "$SHELL" == */zsh ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL" == */bash ]]; then
    if [ "$(uname)" == "Darwin" ]; then
        # На macOS для bash стандартно використовується .bash_profile
        SHELL_RC="$HOME/.bash_profile"
    else
        SHELL_RC="$HOME/.bashrc"
    fi
else
    # Фолбек на випадок інших оболонок
    SHELL_RC="$HOME/.profile"
fi

# 5. Додавання папки до PATH, якщо її там ще немає
PATH_LINE="export PATH=\"\$PATH:$TARGET_DIR\""

if [ -f "$SHELL_RC" ]; then
    if ! grep -Fq "$TARGET_DIR" "$SHELL_RC"; then
        echo "" >> "$SHELL_RC"
        echo "$PATH_LINE" >> "$SHELL_RC"
        echo -e "${GREEN}Successfully added $TARGET_DIR to PATH in $SHELL_RC!${NC}"
    else
        echo -e "${CYAN}$TARGET_DIR is already configured in $SHELL_RC.${NC}"
    fi
else
    # Якщо файлу немає, створюємо його
    echo "$PATH_LINE" > "$SHELL_RC"
    echo -e "${GREEN}Created $SHELL_RC and added $TARGET_DIR to PATH!${NC}"
fi

echo -e "${PURPLE}=======================================${NC}"
echo -e "${YELLOW}Installation complete! Please reload your terminal:${NC}"
echo -e "${CYAN}source $SHELL_RC${NC}"
echo -e "${YELLOW}Or just open a new terminal window.${NC}"
echo -e "${PURPLE}=======================================${NC}"
