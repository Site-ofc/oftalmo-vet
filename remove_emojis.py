import re

def remove_emojis(text):
    # Regex para remover emojis (padrão básico)
    # Emojis e símbolos diversos
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U00002702-\U000027b0"
        "\U000024c2-\U0001f251"
        "]+", flags=re.UNICODE
    )
    # Adicionando outros símbolos comuns que o usuário pode considerar emojis
    text = emoji_pattern.sub(r'', text)
    # Remover ícones manuais se houver (ex: 🔍, 💉, 🏥, ✂️, 📍, 📱, 🌐, ⏰)
    specific_emojis = ["🔍", "💉", "🏥", "✂️", "📍", "📱", "🌐", "⏰", "⚕️", "⚕"]
    for char in specific_emojis:
        text = text.replace(char, '')
    return text

with open('/home/ubuntu/upload/Pasted_content_06.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

clean_content = remove_emojis(content)

with open('/home/ubuntu/oftalmovet/index.html', 'w', encoding='utf-8') as f:
    f.write(clean_content)
