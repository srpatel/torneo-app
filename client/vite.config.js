import { defineConfig, loadEnv } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, path.resolve(process.cwd(), "../"), "");
  return {
    envDir: "..",
    plugins: [svelte()],
    base: env.VITE_CLIENT_BASE_URL + "/",
  };
});
