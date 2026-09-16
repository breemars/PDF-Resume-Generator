import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def html_to_pdf(html_path, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        html_path = Path(html_path).resolve()
        await page.goto(html_path.as_uri())

        await page.pdf(
            path=output_path,
            format="Letter",
            print_background=True,
            margin={
                "top": "0",
                "right": "0",
                "bottom": "0",
                "left": "0"
            }
        )

        await browser.close()


asyncio.run(html_to_pdf("index.html", "resume.pdf"))