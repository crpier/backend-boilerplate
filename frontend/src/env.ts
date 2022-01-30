const env = process.env.VUE_APP_ENV;

let envApiUrl = '';

console.log(`Env is ${env}`)
if (env === 'production') {
  envApiUrl = `https://tiannaru.xyz`;
} else if (env === 'staging') {
  envApiUrl = `https://tiannaru.xyz`;
} else {
  envApiUrl = `https://tiannaru.xyz`;
}

export const apiUrl = "https://tiannaru.xyz";
export const appName = process.env.VUE_APP_NAME;
