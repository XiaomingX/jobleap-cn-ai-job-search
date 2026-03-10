"""Table and markdown formatting functions.
表格和 Markdown 格式化功能。
"""

import re
from datetime import datetime
from typing import Any

from list_updater.constants import FAANG_PLUS, LONG_APPLY_BUTTON, SHORT_APPLY_BUTTON

type Listing = dict[str, Any]


def get_locations(listing: Listing) -> str:
    """Format locations for display in the table.
    格式化要在表格中显示的地点。

    Args:
        listing: A listing dictionary. (列表字典)

    Returns:
        HTML-formatted location string. (HTML 格式的地点字符串)
    """
    locations = "<br>".join(listing["locations"])
    if len(listing["locations"]) <= 3:
        return locations
    num = str(len(listing["locations"])) + " locations"
    return f"<details><summary><strong>{num}</strong></summary>{locations}</details>"


def get_sponsorship(listing: Listing) -> str:
    """Get sponsorship indicator emoji.
    获取签证/赞助指示图标。

    Args:
        listing: A listing dictionary. (列表字典)

    Returns:
        Emoji string for sponsorship status. (签证/赞助状态的图标字符串)
    """
    if listing["sponsorship"] == "Does Not Offer Sponsorship":
        return " 🛂"
    elif listing["sponsorship"] == "U.S. Citizenship is Required":
        return " 🇺🇸"
    return ""


def get_link(listing: Listing) -> str:
    """Generate the application link HTML.
    生成申请链接的 HTML。

    Args:
        listing: A listing dictionary. (列表字典)

    Returns:
        HTML string with application button(s). (包含申请按钮的 HTML 字符串)
    """
    if not listing["active"]:
        return "🔒"

    link = listing["url"]

    # Return standard apply button
    return f'<div align="center"><a href="{link}"><img src="{SHORT_APPLY_BUTTON}" width="50" alt="Apply"></a></div>'


def convert_markdown_to_html(text: str) -> str:
    """Convert markdown formatting to HTML for proper rendering in HTML table cells.
    将 Markdown 格式转换为 HTML，以便在 HTML 表格单元格中正确渲染。

    Args:
        text: Markdown-formatted text. (Markdown 格式的文本)

    Returns:
        HTML-formatted text. (HTML 格式的文本)
    """
    # Convert **bold** to <strong>bold</strong>
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

    # Convert [link text](url) to <a href="url">link text</a>
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    return text


def get_minimal_css() -> str:
    """Return minimal CSS for basic table functionality.

    Returns:
        CSS style string.
    """
    return """
<!-- Minimal table styling for better readability -->
<style>
table { border-collapse: collapse; width: 100%; }
th { text-align: left; font-weight: bold; }
.td-center { text-align: center; }
</style>

"""


def create_md_table(listings: list[Listing], off_season: bool = False) -> str:
    """Create an HTML table from listings.
    从列表创建 HTML 表格。

    Args:
        listings: List of listing dictionaries. (列表字典)
        off_season: Whether this is for off-season listings (includes terms column). (是否为淡季列表（包含条款列）)

    Returns:
        HTML table string. (HTML 表格字符串)
    """
    # Create clean HTML table with minimal styling
    table = "<table>\n<thead>\n<tr>\n"

    if off_season:
        table += "<th>Company</th>\n"
        table += "<th>Role</th>\n"
        table += "<th>Location</th>\n"
        table += "<th>Terms</th>\n"
        table += "<th>Application</th>\n"
        table += "<th>Age</th>\n"
    else:
        table += "<th>Company</th>\n"
        table += "<th>Role</th>\n"
        table += "<th>Location</th>\n"
        table += "<th>Application</th>\n"
        table += "<th>Age</th>\n"

    table += "</tr>\n</thead>\n<tbody>\n"

    prev_company = None
    prev_days_active = None

    for listing in listings:
        # Check if this is a FAANG+ company for fire emoji
        company_name = listing["company_name"]
        is_faang_plus = company_name.lower() in FAANG_PLUS

        raw_url = listing.get("company_url", "").strip()
        company_url = raw_url
        company_markdown = f"**[{company_name}]({company_url})**" if company_url else f"**{company_name}**"

        # Add fire emoji outside the link for FAANG+ companies
        if is_faang_plus:
            company_markdown = f"🔥 {company_markdown}"

        company = convert_markdown_to_html(company_markdown)
        location = get_locations(listing)

        # Check for advanced degree requirements and add graduation cap emoji
        title_with_degree_emoji = listing["title"]

        # Check degrees field for advanced degree requirements
        degrees = listing.get("degrees", [])
        if degrees:
            # Check if only advanced degrees are required (no Bachelor's or Associate's)
            has_bachelors_or_associates = any(degree.lower() in ["bachelor's", "associate's"] for degree in degrees)
            has_advanced_degrees = any(degree.lower() in ["master's", "phd", "mba"] for degree in degrees)

            if has_advanced_degrees and not has_bachelors_or_associates:
                title_with_degree_emoji += " 🎓"

        # Also check title text for degree mentions
        title_lower = listing["title"].lower()
        if any(
            term in title_lower
            for term in ["master's", "masters", "master", "mba", "phd", "ph.d", "doctorate", "doctoral"]
        ):
            if "🎓" not in title_with_degree_emoji:
                title_with_degree_emoji += " 🎓"

        position = title_with_degree_emoji + get_sponsorship(listing)
        terms = ", ".join(listing["terms"])
        link = get_link(listing)

        # Calculate days active
        days_active = (datetime.now() - datetime.fromtimestamp(listing["date_posted"])).days
        days_active = max(days_active, 0)  # in case somehow negative
        if days_active == 0:
            days_display = "0d"
        elif days_active > 30:
            days_display = f"{days_active // 30}mo"
        else:
            days_display = f"{days_active}d"

        # Check if same company and same days active
        if prev_company == company_name and prev_days_active == days_active:
            company = "↳"
        else:
            prev_company = company_name
            prev_days_active = days_active

        # Create HTML table row
        table += "<tr>\n"

        if off_season:
            table += f"<td>{company}</td>\n"
            table += f"<td>{position}</td>\n"
            table += f"<td>{location}</td>\n"
            table += f"<td>{terms}</td>\n"
            table += f"<td>{link}</td>\n"
            table += f"<td>{days_display}</td>\n"
        else:
            table += f"<td>{company}</td>\n"
            table += f"<td>{position}</td>\n"
            table += f"<td>{location}</td>\n"
            table += f"<td>{link}</td>\n"
            table += f"<td>{days_display}</td>\n"

        table += "</tr>\n"

    table += "</tbody>\n</table>\n"
    return table
