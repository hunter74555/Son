import datetime
import os
import getpass  # Более надёжная альтернатива

LOG_FILE = os.path.join(os.path.dirname(__file__), "../memory/run_history.log")


def log_launch(message=""):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)  # Создаём папку memory если её нет
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = getpass.getuser()  # Более стабильный способ
        f.write(f"[{timestamp}] Пользователь {user} запустил /Son. {message}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, default="", help="Дополнительное сообщение для лога")
    args = parser.parse_args()

    log_launch(args.message)
    print("✅ Лог сохранён в", LOG_FILE)