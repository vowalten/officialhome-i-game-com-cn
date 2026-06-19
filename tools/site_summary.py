# tools/site_summary.py
import json
from datetime import date

SITE_DATA = {
    "official_home": {
        "url": "https://officialhome-i-game.com.cn",
        "keywords": ["爱游戏", "官方首页", "游戏平台"],
        "tags": ["官网", "游戏", "平台"],
        "description": "爱游戏官方首页，提供游戏资讯、下载与社区服务。",
        "last_updated": "2025-03-25"
    },
    "game_news": {
        "url": "https://officialhome-i-game.com.cn/news",
        "keywords": ["爱游戏新闻", "行业动态", "游戏更新"],
        "tags": ["新闻", "更新"],
        "description": "爱游戏平台的最新新闻与游戏更新公告。",
        "last_updated": "2025-03-24"
    },
    "game_download": {
        "url": "https://officialhome-i-game.com.cn/download",
        "keywords": ["爱游戏下载", "客户端", "安装包"],
        "tags": ["下载", "客户端"],
        "description": "爱游戏客户端下载中心，支持多平台安装。",
        "last_updated": "2025-03-20"
    },
    "community": {
        "url": "https://officialhome-i-game.com.cn/community",
        "keywords": ["爱游戏社区", "玩家交流", "论坛"],
        "tags": ["社区", "论坛", "交流"],
        "description": "爱游戏玩家社区，分享攻略、心得与反馈。",
        "last_updated": "2025-03-22"
    },
    "support": {
        "url": "https://officialhome-i-game.com.cn/support",
        "keywords": ["爱游戏客服", "帮助中心", "FAQ"],
        "tags": ["客服", "帮助", "FAQ"],
        "description": "爱游戏官方客服与帮助中心，解决玩家问题。",
        "last_updated": "2025-03-18"
    }
}

def build_summary(site_id, record):
    """为单个站点记录生成结构化摘要"""
    lines = []
    lines.append(f"站点标识：{site_id}")
    lines.append(f"URL：{record['url']}")
    lines.append(f"核心关键词：{'、'.join(record['keywords'])}")
    lines.append(f"标签：{'、'.join(record['tags'])}")
    lines.append(f"简短说明：{record['description']}")
    lines.append(f"最后更新：{record['last_updated']}")
    return "\n".join(lines)

def generate_full_report(all_sites):
    """遍历所有站点数据，生成完整摘要报告"""
    report_parts = []
    report_parts.append("=" * 50)
    report_parts.append("爱游戏官方站点结构化摘要报告")
    report_parts.append(f"生成日期：{date.today().isoformat()}")
    report_parts.append("=" * 50)
    for site_id, record in all_sites.items():
        summary = build_summary(site_id, record)
        report_parts.append("")
        report_parts.append(summary)
        report_parts.append("-" * 40)
    report_parts.append("")
    report_parts.append("报告结束。")
    return "\n".join(report_parts)

def export_json(all_sites):
    """将站点数据导出为JSON格式（仅用于展示，不写出文件）"""
    return json.dumps(all_sites, ensure_ascii=False, indent=2)

def main():
    print("开始生成站点摘要...")
    print()

    report = generate_full_report(SITE_DATA)
    print(report)

    print()
    print("--- JSON 预览（前300字符）---")
    json_text = export_json(SITE_DATA)
    print(json_text[:300])

    print()
    print("站点摘要生成完成。")

if __name__ == "__main__":
    main()