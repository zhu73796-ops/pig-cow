#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将本仓库两个 skill 链接到本机发现目录，拒绝覆盖既有技能。"""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents/skills')
    parser.add_argument('--config', type=Path,
                        default=Path.home() / '.config/pnw-skills/paths.json')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    src = repo / 'plugins/pnw-product-planning/skills'
    dest = args.dest.expanduser().resolve()
    config = args.config.expanduser().resolve()
    entries = []
    for name in ('pnw-selling-points', 'pnw-pricing'):
        target = (src / name).resolve()
        if not (target / 'SKILL.md').is_file():
            raise SystemExit('缺少源技能：' + name)
        path = dest / name
        same = path.is_symlink() and path.resolve() == target
        if (path.exists() or path.is_symlink()) and not same:
            raise SystemExit('已有技能或其他链接，未做改动：' + str(path))
        entries.append((path, target, same))
    if config.exists() and not config.is_file():
        raise SystemExit('配置位置不是文件，未做改动：' + str(config))
    for path, target, same in entries:
        print(('已有相同链接：' if same else '将创建链接：') + str(path) + ' -> ' + str(target))
    print(('保留已有配置：' if config.exists() else '将初始化配置（需填真实路径）：') + str(config))
    if args.dry_run:
        print('检查完成；没有写入。')
        return
    dest.mkdir(parents=True, exist_ok=True)
    for path, target, same in entries:
        if not same:
            path.symlink_to(target, target_is_directory=True)
    if not config.exists():
        config.parent.mkdir(parents=True, exist_ok=True)
        with config.open('x') as stream:
            json.dump({'business_root': None, 'assets_root': None, 'skills_root': None},
                      stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    print('技能安装完成。请配置真实资料路径，下一轮检查技能发现与资料访问。')


if __name__ == '__main__':
    main()
