// ./app/page.tsx
import ClientComponent from "@/components/ClientComponent";

import { fetchAccessToken } from "hume";

export default async function Page() {
  const accessToken = await fetchAccessToken({
    apiKey: String(process.env.HUME_API_KEY),
    secretKey: String(process.env.HUME_SECRET_KEY),
  });

  if (!accessToken) {
    throw new Error();
  }
  return (
    <ClientComponent
      configKey={process.env.HUME_CONFIG_KEY}
      accessToken={accessToken}
    />
  );
}
