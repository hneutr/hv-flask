from pathlib import Path
import networks

if __name__ == '__main__':
    cwd = Path.cwd().joinpath('networks')
    templates_dir = cwd.joinpath('templates')
    pages_dir = cwd.joinpath('pages')
    static_dir = cwd.joinpath('static')

    networks.regenerate(
        pages_directory=pages_dir,
        static_directory=static_dir,
        templates_directory=templates_dir,
    )
