"""List Updater CLI - Internship listing management tool.
列表更新 CLI - 实习岗位列表管理工具。
"""

from pathlib import Path

import typer

from list_updater import (
    cmd_contribution_process,
    cmd_listings_diff,
    cmd_listings_fix,
    cmd_listings_mark_inactive,
    cmd_listings_search,
    cmd_listings_stats,
    cmd_listings_validate,
    cmd_readme_update,
)

app = typer.Typer(
    name="list-updater",
    help="Internship listing management CLI for GitHub Actions (GitHub Actions 的实习列表管理命令行工具)",
    no_args_is_help=True,
)

# =============================================================================
# README Commands (README 相关命令)
# =============================================================================

readme_app = typer.Typer(help="README operations (README 操作)")
app.add_typer(readme_app, name="readme")


@readme_app.command("update")
def readme_update() -> None:
    """Update README files from listings.json (从 listings.json 更新 README 文件)。"""
    cmd_readme_update()


# =============================================================================
# Contribution Commands (贡献相关命令)
# =============================================================================

contribution_app = typer.Typer(help="Contribution processing (贡献处理)")
app.add_typer(contribution_app, name="contribution")


@contribution_app.command("process")
def contribution_process(
    event_file: Path = typer.Argument(..., help="Path to GitHub event JSON file (GitHub 事件 JSON 文件路径)"),
) -> None:
    """Process an approved contribution issue (new/edit internship) (处理已批准的贡献 issue（新增/编辑实习）)。"""
    cmd_contribution_process(str(event_file))


# =============================================================================
# Listings Commands (列表管理命令)
# =============================================================================

listings_app = typer.Typer(help="Listings management and analytics (列表管理与分析)")
app.add_typer(listings_app, name="listings")


@listings_app.command("mark-inactive")
def listings_mark_inactive(
    event_file: Path = typer.Argument(..., help="Path to GitHub event JSON file (GitHub 事件 JSON 文件路径)"),
) -> None:
    """Bulk mark listings as inactive from a GitHub issue (从 GitHub issue 批量将列表标记为不活跃)。"""
    cmd_listings_mark_inactive(str(event_file))


@listings_app.command("stats")
def listings_stats(
    json_output: bool = typer.Option(False, "--json", help="Output as JSON (以 JSON 格式输出)"),
) -> None:
    """Show listing statistics (counts, categories, top companies) (显示列表统计信息（计数、类别、顶级公司）)。"""
    cmd_listings_stats(json_output=json_output)


@listings_app.command("validate")
def listings_validate(
    fix: bool = typer.Option(False, "--fix", help="Attempt to auto-fix issues (尝试自动修复问题)"),
) -> None:
    """Validate listings.json schema and data integrity (验证 listings.json 结构和数据完整性)。"""
    cmd_listings_validate(fix=fix)


@listings_app.command("search")
def listings_search(
    company: str | None = typer.Option(None, "--company", "-c", help="Filter by company name (按公司名称过滤)"),
    title: str | None = typer.Option(None, "--title", "-t", help="Filter by job title (按职位头衔过滤)"),
    location: str | None = typer.Option(None, "--location", "-l", help="Filter by location (按地点过滤)"),
    category: str | None = typer.Option(None, "--category", help="Filter by category (按类别过滤)"),
    active: bool = typer.Option(False, "--active", help="Show only active listings (仅显示活跃列表)"),
    inactive: bool = typer.Option(False, "--inactive", help="Show only inactive listings (仅显示不活跃列表)"),
    limit: int = typer.Option(20, "--limit", "-n", help="Maximum results to show (显示的最多结果数)"),
) -> None:
    """Search and filter listings (搜索并过滤列表)。"""
    cmd_listings_search(
        company=company,
        title=title,
        location=location,
        category=category,
        active_only=active,
        inactive_only=inactive,
        limit=limit,
    )


@listings_app.command("diff")
def listings_diff(
    since: str | None = typer.Option(None, "--since", help="Show changes since date (YYYY-MM-DD) (显示自指定日期以来的变化)"),
    commit: str | None = typer.Option(None, "--commit", help="Show changes since git commit (显示自指定 git commit 以来的变化)"),
) -> None:
    """Show changes to listings since a date or commit (显示自日期或 commit 以来的列表变化)。"""
    cmd_listings_diff(since=since, commit=commit)


@listings_app.command("fix")
def listings_fix(
    dry_run: bool = typer.Option(False, "--dry-run", help="Show fixes without saving (仅显示修复而不保存)"),
    issue_type: str | None = typer.Option(None, "--type", help="Only fix specific type: empty, duplicate, blocked (仅修复特定类型：空、重复、被屏蔽)"),
    auto: bool = typer.Option(False, "--auto", help="Auto-accept all recommended fixes (自动接受所有建议的修复)"),
) -> None:
    """Interactively fix issues in listings.json (交互式修复 listings.json 中的问题)。"""
    cmd_listings_fix(dry_run=dry_run, issue_type=issue_type, auto=auto)


if __name__ == "__main__":
    app()
