#!/usr/bin/env python3
"""Split the two monolithic API docs into focused sub-pages so the site
uses a real left-hand nav tree instead of one giant scrolling page."""
import os
import re

VENDORS_SPLITS = [
    (1, 253, "vendors/overview.md", "Overview & Authentication"),
    (254, 538, "vendors/menu.md", "Menu Management"),
    (539, 686, "vendors/availability.md", "Availability & Timing"),
    (687, 970, "vendors/orders.md", "Orders & Webhooks"),
    (971, 1116, "vendors/categories.md", "Categories"),
    (1117, 1419, "vendors/products.md", "Products"),
    (1420, 1646, "vendors/promotions.md", "Promotions & Inventory"),
    (1647, 1691, "vendors/order-status.md", "Order Status Updates"),
]

LOGISTICS_SPLITS = [
    (1, 80, "logistics/add-order.md", "Add Order"),
    (81, 104, "logistics/overview.md", "Overview & Authentication"),
    (105, 163, "logistics/cancel-order.md", "Cancel Order"),
    (164, 220, "logistics/return-order.md", "Return Order"),
    (221, 309, "logistics/order-status.md", "Get Order Status"),
    (310, 330, "logistics/errors.md", "Error Handling"),
    (331, 522, "logistics/webhook-status.md", "Change Status Webhook"),
    (523, 581, "logistics/webhook-driver-location.md", "Driver Location Webhook"),
]

TITLE_RE = re.compile(r"^# .*$", re.MULTILINE)


def split(src_path, splits, asset_prefix_fix):
    with open(src_path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    for start, end, rel_out, title in splits:
        chunk = lines[start - 1:end]
        text = "\n".join(chunk)
        # drop the old whole-document H1 if it's in this chunk
        text = TITLE_RE.sub("", text, count=1) if "# " in text[:200] else text
        text = text.strip("\n")
        text = text.replace("(assets/", "(../assets/")
        out_path = os.path.join("docs", rel_out)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{text}\n")
        print("wrote", out_path)


if __name__ == "__main__":
    split("docs/vendors-api.md", VENDORS_SPLITS, "vendors")
    split("docs/logistics-api.md", LOGISTICS_SPLITS, "logistics")
