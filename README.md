# 粉与白卖点与价格技能｜鹿比交付版

版本 0.2.0，更新于 2026-10-12（交付目录沿用 20261006）。目标仓库：https://github.com/zhu73796-ops/pig-cow 。本仓库分发两个技能，尚未在鹿比电脑验收。包内包含工作规则、定价参数和 Jeff 的案例审核；业务资料接入见 [TRANSFER.md](TRANSFER.md)。

## 包含什么

- `plugins/pnw-product-planning/skills/pnw-selling-points/`：完整卖点技能，以团队/Brief 主线为起点，AI 调研补充，按页面意图生成有证据的销售型表达。
- `plugins/pnw-product-planning/skills/pnw-pricing/`：完整价格技能，AJ 不重复计费、红线与竞品比较、7/8/9 尾数整理，输出待批准方案。
- 58 例带日期的文字审核快照，保留 51/4/3 判断与未澄清范围；不附主图文件。
- 插件清单、仓库 marketplace、安装脚本、路径配置示例和外部依赖表。

本次同步 Jeff 当前已更新的技能：销售型卖点统一对应团队“买点”；新增三平台统一销售色名与SKU关联；买点与原A内价格确认后才进入正式视觉策划。商业定价参数未改变，案例快照不可替代当前商品事实。鹿比原买点定义全文尚未在当前挂载盘读取，用语对应依据Jeff本次明确确认。

## 鹿比安装：先采用单独技能方式

1. 获得仓库读取权限，将仓库 clone 到电脑一个固定目录。保持目录固定，供后续技能链接安装和更新使用。
2. 在 Codex 中打开该目录，发送：

> 按 README 安装粉与白卖点和价格技能。先用 scripts/install.py --dry-run 检查，再执行安装；遇到已存在技能先报告，不覆盖。帮我核实并配置 ~/.config/pnw-skills/paths.json 中的真实资料路径。

终端也可在仓库根目录运行 `python3 scripts/install.py --dry-run`，检查后运行 `python3 scripts/install.py`。默认创建当前用户 `~/.agents/skills` 下的两个符号链接，指向固定仓库。现有目录或不同链接会停止，不覆盖。不能删除或移动仓库后继续依赖这些链接。

3. 在初始化配置中填入三个真实绝对目录，按 [DEPENDENCIES.md](DEPENDENCIES.md) 核对资料。安装成功不等于资料齐全。
4. 下一轮对话测试：

> 使用 $pnw-selling-points，先检查路径，读取指定项目已有选品／样品／Brief 与素材，输出买点（销售型卖点）候选与三平台统一销售色名关联，并报告 Obsidian 保存和确认状态；未确认时不进入正式视觉策划。

价格测试先核对真实产品身份、生效 AJ、等级和渠道；缺失时报告，不代猜。界面未识别新技能时重启 Codex 后复查。

## 插件方式（可选）

已准备 portable `plugin.json`、Codex 兼容清单和 `.agents/plugins/marketplace.json`。在支持 repo marketplace 的 Codex 环境中可从该源安装、启用。没有 MCP 或连接器，不会自动提供产品库、Obsidian 或账号访问权限。插件和单独技能安装选一种，避免重复发现。尚未在鹿比的应用版本实测插件安装。

## 从 GitHub 单独安装（另一种方式）

若目标电脑有 skill-installer，也可让 Codex 安装仓库中的这两个目录：

- `plugins/pnw-product-planning/skills/pnw-selling-points`
- `plugins/pnw-product-planning/skills/pnw-pricing`

私有仓库须有实际读取凭据；仍需初始化 `~/.config/pnw-skills/paths.json`，可参照 `config/paths.example.json`。安装器采取复制方式时，拉取仓库不会更新已安装副本，后续要另行更新，不能同时再运行本包链接安装。

## 后续更新

Jeff 审定新版后提交 GitHub；鹿比在无本地冲突的仓库运行 `git pull --ff-only`。默认链接安装随仓库文件变化，当前对话可能已加载旧规则，更新后在下一轮复查。插件或复制安装按相应来源刷新，不假定提交 GitHub 自动更新所有电脑。业务采用及线上改价仍由对应负责人确认。

`PACKAGE_MANIFEST.json` 记录源文件及交付文件摘要；哈希只核对文件内容，不证明商业有效性。

官方依据：[技能发现与符号链接](https://learn.chatgpt.com/docs/build-skills)、[插件与 marketplace](https://developers.openai.com/plugins/build/plugins)。
