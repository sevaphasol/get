## 1. Как создать SSH-ключ

SSH-ключ используется для безопасной аутентификации при работе с GitHub. Чтобы создать SSH-ключ, выполните следующие шаги:

### Генерация SSH ключа

1. Откройте Терминал. Вставьте в него следующий код, подставив в кавычки свой адрес электронной почты на GitHub.
2. Выполните комманду
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
3. Эта команда создает новый ключ SSH, используя введенный адрес электронной почты.
    ```bash
    > Generating public/private ed25519 key pair.
    ```
4. После вам будет предложено ввести название файла, в который сохранится ключ. Нажмите Enter, чтобы принять предложенное название и
расположение файла по умолчанию.
    ```bash
    > Enter a file in which to save the key (/Users/you/.ssh/id_ed25519): [Press enter]
    ```
5. Не используйте пароль при генерации ключа
    ```bash
    > Enter passphrase (empty for no passphrase): [Press enter]
    > Enter same passphrase again: [Press enter]
    ```

### Добавление ключа в ssh-агент

1. Запустите в терминале shh-agent.
    ```bash
    eval "$(ssh-agent -s)"
    > Agent pid 59566
    ```
2. Добавьте свой приватный ключ SSH в ssh-agent. Если вы создали свой ключ под другим именем, замените id_ed25519 в команде именем вашего приватного ключа.
    ```bash
    $ ssh-add ~/.ssh/id_ed25519
    ```

## 2. Добавление ключа на сайт

1. Скопируйте содержание файла SSH ключа в буфер обмена
2. Откройте настройки пользователя (Settings) и выберите раздел SSH and GPG keys, или перейдите по ссылке https://github.com/settings/keys.
3. Кликните на New SSH key или Add SSH key.
4. В поле «Title» добавьте описание нового ключа.
5. Вставьте ключ из буфера обмена в поле Key.
6. Нажмите "Add SSH key". Если будет предложено, введите пароль для подтверждения.

## 3. Клонирование репозитория по SSH ключу

Когда вы решите склонировать репозиторий, нужно нажать кнопку Clone, но вместо HTTPS выбрать SSH. Скопировать ссылку и выполнить
команду git clone "скопированная ссылка"
