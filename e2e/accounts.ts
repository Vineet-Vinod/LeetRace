import { createClerkClient } from "@clerk/backend";
import { clerk } from "@clerk/testing/playwright";
import type { Page } from "@playwright/test";

export type TestAccount = {
  email: string;
  username: string;
};

export async function createTestAccount(): Promise<TestAccount> {
  const secretKey = process.env.CLERK_SECRET_KEY;
  if (!secretKey?.startsWith("sk_test_")) {
    throw new Error("Multi-user tests require a Clerk development secret key (sk_test_*).");
  }

  const suffix = crypto.randomUUID().replaceAll("-", "").slice(0, 10);
  const account = {
    email: `leetrace+clerk_test_${suffix}@example.com`,
    username: `p${suffix.slice(0, 9)}`,
  };
  const backend = createClerkClient({ secretKey });
  await backend.users.createUser({
    emailAddress: [account.email],
    username: account.username,
    firstName: "LeetRace",
    lastName: "E2E",
    password: `TerseCodes-E2E-${suffix}!`,
  });

  return account;
}

export async function signInTestAccount(page: Page, account: TestAccount): Promise<void> {
  await page.goto("/");
  await clerk.signIn({ page, emailAddress: account.email });
  await page.getByRole("navigation", { name: "Account" }).waitFor({ state: "visible" });
}
