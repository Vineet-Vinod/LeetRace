import { test, expect, openPage } from "./fixtures";

test("redirects signed-out room links through sign-in and preserves the invite", async ({ page }) => {
  await openPage(page, "/join/ABC123");

  await expect(page).toHaveURL(/\/sign-in\?/);
  const current = new URL(page.url());
  expect(current.searchParams.get("redirect_url")).toBe("/join/ABC123");
  await expect(page.locator(".cl-signIn-root")).toBeVisible();
  await expect(page.getByRole("link", { name: /sign up/i })).toBeVisible();
});

test("creates a scoped development account through Clerk signup", async ({ page }) => {
  const suffix = crypto.randomUUID().replaceAll("-", "").slice(0, 10);
  const email = `leetrace+clerk_test_${suffix}@example.com`;
  const username = `t${suffix.slice(0, 9)}`;

  await openPage(page, "/sign-up");
  await expect(page.locator(".cl-signUp-root")).toBeVisible();

  await fillIfVisible(page, 'input[name="firstName"]', "LeetRace");
  await fillIfVisible(page, 'input[name="lastName"]', "E2E");
  await fillIfVisible(page, 'input[name="username"]', username);
  await page.locator('input[name="emailAddress"]').fill(email);
  await fillIfVisible(page, 'input[name="password"]', "TerseCodes-E2E-2026!");
  const phone = page.locator('input[name="phoneNumber"]');
  if (await phone.isVisible().catch(() => false)) await phone.fill("+15555550100");
  const legal = page.locator('input[name="legalAccepted"]');
  if (await legal.isVisible().catch(() => false)) await legal.check();

  await page.getByRole("button", { name: "Continue", exact: true }).click();
  const code = page.getByRole("textbox", { name: /verification code/i });
  if (await code.isVisible({ timeout: 5_000 }).catch(() => false)) {
    await code.pressSequentially("424242");
  }

  await expect(page).toHaveURL((url) => !url.pathname.startsWith("/sign-up"), { timeout: 30_000 });
  await expect(page.getByRole("navigation", { name: "Account" })).toBeVisible({ timeout: 30_000 });
});

async function fillIfVisible(
  page: import("@playwright/test").Page,
  selector: string,
  value: string,
): Promise<void> {
  const field = page.locator(selector);
  if (await field.isVisible().catch(() => false)) await field.fill(value);
}
