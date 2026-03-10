"""README generation and embedding functions.
README 生成和嵌入功能。
"""

from typing import Any

from list_updater.category import create_category_table, ensure_categories
from list_updater.constants import CATEGORIES, GITHUB_FILE_SIZE_LIMIT, SIZE_BUFFER
from list_updater.listings import filter_active, mark_stale_listings

type Listing = dict[str, Any]


def check_and_insert_warning(content: str, repo_name: str = "Summer2026-Internships") -> str:
    """Insert warning notice before GitHub cutoff point while preserving full content.
    在 GitHub 截断点之前插入警告通知，同时保留完整内容。

    Args:
        content: The README content. (README 内容)
        repo_name: The repository name for links. (用于链接的代码库名称)

    Returns:
        Content with warning inserted if necessary. (如果需要，返回插入了警告的内容)
    """
    content_size = len(content.encode("utf-8"))

    if content_size <= (GITHUB_FILE_SIZE_LIMIT - SIZE_BUFFER):
        return content

    # Find insertion point right at the GitHub cutoff (with minimal buffer for the warning itself)
    # Use a smaller buffer so the warning appears right at the cutoff, not before it
    target_size = GITHUB_FILE_SIZE_LIMIT - SIZE_BUFFER

    # Convert to bytes for accurate measurement (转换为字节以进行准确测量)
    content_bytes = content.encode("utf-8")

    # Find the last complete table row before the limit (找到限制前的最后一行完整表格行)
    insertion_bytes = content_bytes[:target_size]
    insertion_content = insertion_bytes.decode("utf-8", errors="ignore")

    # Find the last complete </tr> tag to ensure clean insertion (找到最后一个完整的 </tr> 标签以确保干净地插入)
    last_tr_end = insertion_content.rfind("</tr>")
    if last_tr_end != -1:
        # Find the end of this row
        next_tr_start = insertion_content.find("\n", last_tr_end)
        if next_tr_start != -1:
            insertion_point = next_tr_start
        else:
            insertion_point = last_tr_end + 5  # After </tr>
    else:
        insertion_point = len(insertion_content)

    # Create the warning notice with anchor link
    warning_notice = f"""
</tbody>
</table>

---

<div align="center" id="github-cutoff-warning">
  <h2>🔗 See Full List (查看完整列表)</h2>
  <p><strong>⚠️ GitHub preview cuts off around here due to file size limits. (由于文件大小限制，GitHub 预览在此处被截断。)</strong></p>
  <p>📋 <strong><a href="./README.md#-see-full-list">Click here to view the complete list with all internship opportunities! (点击此处查看包含所有实习机会的完整列表！)</a></strong> 📋</p>
</div>

---

<table>
<thead>
<tr>
<th>Company</th>
<th>Role</th>
<th>Location</th>
<th>Application</th>
<th>Age</th>
</tr>
</thead>
<tbody>
"""

    # Split content at insertion point and insert warning
    before_insertion = content[:insertion_point]
    after_insertion = content[insertion_point:]

    return before_insertion + warning_notice + after_insertion


def embed_table(
    listings: list[Listing],
    filepath: str,
    off_season: bool = False,
    active_only: bool = False,
    inactive_only: bool = False,
) -> None:
    """Embed the listings table into a README file.
    将列表表格嵌入 README 文件。

    Args:
        listings: List of listing dictionaries. (列表字典)
        filepath: Path to the README file to modify. (要修改的 README 文件路径)
        off_season: Whether this is for off-season listings. (是否为淡季列表)
        active_only: If True, only include active listings (no inactive sections). (如果为 True，仅包含活跃列表)
        inactive_only: If True, only include inactive listings. (如果为 True，仅包含不活跃列表)
    """
    # Ensure all listings have a category
    listings = ensure_categories(listings)
    listings = mark_stale_listings(listings)

    # Filter listings based on active/inactive mode
    if inactive_only:
        filtered_listings = [listing for listing in listings if not listing.get("active", False)]
        total_count = len(filtered_listings)
    else:
        # For active_only or default, count active listings
        active_listings = filter_active(listings)
        total_count = len(active_listings)

    # Count listings by category
    category_counts: dict[str, int] = {}
    for category_info in CATEGORIES.values():
        cat_name = category_info["name"]
        if inactive_only:
            count = len(
                [
                    listing
                    for listing in listings
                    if listing["category"] == cat_name and not listing.get("active", False)
                ]
            )
        else:
            count = len(
                [listing for listing in listings if listing["category"] == cat_name and listing.get("active", False)]
            )
        category_counts[cat_name] = count

    # Build the category summary for the Browse section
    category_order = ["Software", "Product", "AI/ML/Data", "Quant", "Hardware"]
    category_links = []

    # Use the appropriate README file based on whether this is off-season or not
    if inactive_only:
        readme_filename = "README-Inactive.md"
    elif off_season:
        readme_filename = "README-Off-Season.md"
    else:
        readme_filename = "README.md"
    github_readme_base = f"./{readme_filename}"

    for category_key in category_order:
        if category_key in CATEGORIES:
            category_info = CATEGORIES[category_key]
            name = category_info["name"]
            emoji = category_info["emoji"]
            count = category_counts[name]
            anchor = name.lower().replace(" ", "-").replace(",", "").replace("&", "")
            if inactive_only:
                link = f"{github_readme_base}#-{anchor}-internship-roles-inactive"
            else:
                link = f"{github_readme_base}#-{anchor}-internship-roles"
            category_links.append(f"{emoji} **[{name}]({link})** ({count})")

    category_counts_str = "\n\n".join(category_links)

    new_text = ""
    in_browse_section = False
    browse_section_replaced = False
    in_table_section = False

    with open(filepath) as f:
        for line in f.readlines():
            if not browse_section_replaced and line.startswith("### Browse"):
                in_browse_section = True
                if inactive_only:
                    header = f"### Browse {total_count} Inactive Internship Roles by Category"
                else:
                    header = f"### Browse {total_count} Internship Roles by Category"
                new_text += f"{header}\n\n{category_counts_str}\n\n---\n"
                browse_section_replaced = True
                continue

            if in_browse_section:
                if line.startswith("---"):
                    in_browse_section = False
                continue

            if not in_table_section and "TABLE_START" in line:
                in_table_section = True
                new_text += line
                new_text += "\n---\n\n"

                # Add tables for each category in order
                for category_key in category_order:
                    if category_key in CATEGORIES:
                        category_info = CATEGORIES[category_key]
                        table = create_category_table(
                            listings,
                            category_info["name"],
                            off_season,
                            active_only=active_only,
                            inactive_only=inactive_only,
                        )
                        if table:
                            new_text += table
                continue

            if in_table_section:
                if "TABLE_END" in line:
                    in_table_section = False
                    new_text += line
                continue

            if not in_browse_section and not in_table_section:
                new_text += line

    # Check content size and insert warning if necessary (only for main README, not inactive)
    if not inactive_only:
        final_content = check_and_insert_warning(new_text)
    else:
        final_content = new_text

    with open(filepath, "w") as f:
        f.write(final_content)
