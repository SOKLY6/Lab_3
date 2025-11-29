import sys
import typer
from cli import cli, show_help
from logger.logger_setup import logger


def main() -> None:
    """Точка входа с обработкой всех ошибок."""
    typer.echo('=== CLI для работы с алгоритмами ===')
    typer.echo('Вводите команды построчно.')
    typer.echo("Введите 'exit' или нажмите Ctrl+D для выхода.")
    typer.echo("Введите 'help' для справки.")
    typer.echo()

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        if line.lower() in ['exit', 'quit']:
            typer.echo('Выход из программы.')
            logger.info('Программа завершена пользователем')
            break

        if line.lower() == 'help':
            show_help()
            continue

        old_argv = sys.argv
        try:
            sys.argv = ['main.py'] + line.split()
            logger.info(f'Выполнение команды: {line}')
            cli()
        except SystemExit:
            pass
        except ValueError as e:
            print(f'Ошибка значения: {e}', file=sys.stderr)
            logger.error(f'ValueError при выполнении команды "{line}": {e}')
        except TypeError as e:
            print(f'Ошибка типа: {e}', file=sys.stderr)
            logger.error(f'TypeError при выполнении команды "{line}": {e}')
        except Exception as e:
            print(f'Ошибка выполнения команды: {e}')
            logger.error(
                f'Неожиданная ошибка при выполнении команды "{line}": {e}'
            )
        finally:
            sys.argv = old_argv


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Команда завершена пользователем')
        logger.info('Команда завершена пользователем')
