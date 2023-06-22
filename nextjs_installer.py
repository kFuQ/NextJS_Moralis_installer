import os
import subprocess

class NextJsApp:
    def __init__(self):
        self.project_name = ""

    def create_project(self, project_name):
        self.project_name = project_name
        os.mkdir(project_name)
        os.chdir(project_name)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.run_command('npx -y create-next-app . --import-alias="@/*" --ts --tailwind --eslint --app --src-dir --use-npm', '\n\n\nInstalling Your App\n\nPls wait kthxbai\n')
        os.system('cls' if os.name == 'nt' else 'clear')
        self.run_command('npm install moralis @moralisweb3/next next-auth wagmi viem @vercel/analytics react-wrap-balancer next-pwa lucide-react', '\n\n\nInstalling Moralis Dependencies\n')
        os.system('cls' if os.name == 'nt' else 'clear')
        self.run_command('npm up', '\n\n\nUpdating NodeJS Packages\n')
        os.system('cls' if os.name == 'nt' else 'clear')
        self.add_files()

    def run_command(self, command, message):
        print(message)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ''
        for line in process.stdout:
            line = line.decode('utf-8').strip()
            print(line)  # print the progress in the terminal
            output += line
        retval = process.wait()
        return output
        os.system('cls' if os.name == 'nt' else 'clear')



        with open('pubic/browserconfig.xml', 'w') as f:
            f.write("""
    <?xml version="1.0" encoding="utf-8"?>
    <browserconfig>
      <msapplication>
        <tile>
          <square70x70logo src="/icons/ms-icon-70x70.webp"/>
          <square144x144logo src="/icons/ms-icon-144x144.webp"/>
          <square150x150logo src="/icons/ms-icon-150x150.webp"/>
          <square310x310logo src="/icons/ms-icon-310x310.webp"/>
          <TileColor>#ffffff</TileColor>
        </tile>
      </msapplication>
    </browserconfig>
            """)

        with open('public/manifest.json', 'w') as f:
            f.write("""
    {
    "screenshots": [
      {
        "src": "/screenshots/screen-1.png",
        "sizes": "1434x949",
        "type": "image/png",
        "description": "Home Screen"
      },
      {
        "src": "/screenshots/screen-2.png",
        "sizes": "658x947",
        "type": "image/png",
        "description": "Home Screen Small"
      }
    ],
      "name": "NextJS Moralis Framework Demo",
      "applicationName": "NextJS Moralis Framework Demo",
      "appWebApp": true,
      "background_color": "#000",
      "categories": [
        "cars",
        "design",
        "developer",
        "finance",
        "multimedia",
        "network",
        "networking",
        "photo &amp; video",
        "photo",
        "social"
      ],
      "description": "NextJS Moralis Framework Demo Badass website",
      "dir": "auto",
      "display": "standalone",
      "display_override": ["window-controls-overlay"],
      "edge_side_panel": { "preferred_width": 400 },
      "handle_links": "preferred",
      "language": "en",

      "icons": [
    	{
    		"src": "/icons/android-icon-36x36.webp",
    		"sizes": "36x36",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "0.75"
    	},
    	{
    		"src": "/icons/android-icon-48x48.webp",
    		"sizes": "48x48",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "1.0"
    	},
    	{
    		"src": "/icons/android-icon-72x72.webp",
    		"sizes": "72x72",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "1.5"
    	},
    	{
    		"src": "/icons/android-icon-96x96.webp",
    		"sizes": "96x96",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "2.0"
    	},
    	{
    		"src": "/icons/android-icon-144x144.webp",
    		"sizes": "144x144",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "3.0"
    	},
    	{
    		"src": "/icons/android-icon-192x192.webp",
    		"sizes": "192x192",
    		"type": "image/webp",
    		"purpose": "any",
    		"density": "4.0"
    	},
        {
          "src": "/icons/manifest-icon-192.maskable.png",
          "sizes": "192x192",
          "type": "image/png",
          "purpose": "any"
        },
        {
          "src": "/icons/manifest-icon-192.maskable.png",
          "sizes": "192x192",
          "type": "image/png",
          "purpose": "maskable"
        },
        {
          "src": "/icons/manifest-icon-512.maskable.png",
          "sizes": "512x512",
          "type": "image/png",
          "purpose": "any"
        },
        {
          "src": "/icons/manifest-icon-512.maskable.png",
          "sizes": "512x512",
          "type": "image/png",
          "purpose": "maskable"
        }
      ],
      "id": "/?source=pwa",
      "launch_handler": {
        "client_mode": "auto"
      },
      "msapplication_config": "/browserconfig.xml",
      "msapplication_TileColor": "#FF000",
      "orientation": "any",
      "prefer_related_applications": false,
      "protocol_handlers": [
        {
          "protocol": "mailto",
          "url": "/mail?type=%s"
        },
        {
          "protocol": "tel",
          "url": "/tele?type=%s"
        },
        {
          "protocol": "ipfs",
          "url": "/ipfs?type=%s"
        },
        {
          "protocol": "sms",
          "url": "/sms?type=%s"
        },
        {
          "protocol": "smsto",
          "url": "/smsto?type=%s"
        }
      ],
      "scope": "/",
      "scope_extensions": [
        {"origin": "*.vercel.app"},
      ],

      "short_name": "NextJS Demo",
      "start_url": "/?source=pwa",
      "shortcuts": [
        {
          "name": "About",
          "short_name": "About",
          "description": "About Page",
          "url": "/about?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        },
        {
          "name": "Crypto",
          "short_name": "Crypto",
          "description": "Trade Crypto",
          "url": "/tradecrypto?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        },
        {
          "name": "Facebook",
          "short_name": "Facebook",
          "description": "Follow me on Facebook",
          "url": "/facebook?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        },
        {
          "name": "Github",
          "short_name": "Github",
          "description": "Github",
          "url": "/github?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        },
        {
          "name": "Instagram",
          "short_name": "Instagram",
          "description": "Instagram",
          "url": "/instagram?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        },
        {
          "name": "Twitter",
          "short_name": "Twitter",
          "description": "Follow Me on Twitter",
          "url": "/twitter?source=pwa",
          "icons": [
            {
              "src": "/icons/android-icon-96x96.webp",
              "sizes": "96x96"
            }
          ]
        }
      ],
      "theme_color": "#ff0000",
      "theme_colors": [
        {
          "color": "#FFF00",
          "media": "(prefers-color-scheme: dark)"
        },
        {
          "color": "#FFF",
          "media": "(prefers-color-scheme: light)"
        }
      ]
    }
                """)

    def add_files(self):
        with open('.env.local', 'w') as f:
            f.write("""
    ### These env vars are for authentication & database to work. If you don't require them, feel free to enter dummy values for all these.
    APP_DOMAIN=vercel.app
    REACT_APP_MORALIS_API_KEY=
    REACT_URL=http://localhost:3000
    AUTH_SECRET=

    # Create a free PostgreSQL database: https://vercel.com/postgres
    # If you're deploying this template with a Vercel Deploy Button, these will be configured automatically for you.
    POSTGRES_URL=""
    POSTGRES_PRISMA_URL=""
    POSTGRES_URL_NON_POOLING=""
    POSTGRES_USER="default"
    POSTGRES_HOST=""
    POSTGRES_PASSWORD=""
    POSTGRES_DATABASE=""

    # Follow the instructions here to create a Google OAuth app: https://refine.dev/blog/nextauth-google-github-authentication-nextjs/#for-googleprovider-make-sure-you-have-a-google-account
    GOOGLE_CLIENT_ID=
    GOOGLE_CLIENT_SECRET=
    GITHUB_ID=
    GITHUB_SECRET=
    ZOOM_SECRET_TOKEN=

    # Only for production – generate one here: https://generate-secret.vercel.app/32
    NEXTAUTH_SECRET=
    ## Only required for localhost
    NEXTAUTH_URL=http://localhost:3000


                """)

        os.mkdir('pages')
        with open('pages/_app.jsx', 'w') as f:
            f.write("""
import { createConfig, configureChains, WagmiConfig } from "wagmi";
import { publicProvider } from "wagmi/providers/public";
import { SessionProvider } from "next-auth/react";
import { mainnet } from "wagmi/chains";

const { publicClient, webSocketPublicClient } = configureChains([mainnet],[publicProvider()]);

const config = createConfig({
  autoConnect: true,
  publicClient,
  webSocketPublicClient,
});

function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig config={config}>
      <SessionProvider session={pageProps.session} refetchInterval={0}>
        <Component {...pageProps} />
      </SessionProvider>
    </WagmiConfig>
  );
}

export default MyApp;
            """)

        os.mkdir('pages/api')
        os.mkdir('pages/api/auth')
        with open('pages/api/auth/[...nextauth].js', 'w') as f:
            f.write("""
import NextAuth from "next-auth";
import { MoralisNextAuthProvider } from "@moralisweb3/next";

export default NextAuth({
  providers: [MoralisNextAuthProvider()],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.user = user;
      }
      return token;
    },
    async session({ session, token }) {
      session.user = token.user;
      return session;
    },
  },
});
            """)

        os.mkdir('pages/api/moralis')
        with open('pages/api/moralis/[...moralis].ts', 'w') as f:
            f.write("""
import { MoralisNextApi } from "@moralisweb3/next";

export default MoralisNextApi({
  apiKey: process.env.REACT_APP_MORALIS_API_KEY,
  authentication: {
    domain: "amazing.dapp",
    uri: process.env.NEXTAUTH_URL,
    timeout: 120,
  },
});
            """)

        with open('pages/signin.jsx', 'w') as f:
            f.write("""
import { MetaMaskConnector } from "wagmi/connectors/metaMask";
import { signIn } from "next-auth/react";
import { useAccount, useConnect, useSignMessage, useDisconnect } from "wagmi";
import { useRouter } from "next/router";
import { useAuthRequestChallengeEvm } from "@moralisweb3/next";

function SignIn() {
  const { connectAsync } = useConnect();
  const { disconnectAsync } = useDisconnect();
  const { isConnected } = useAccount();
  const { signMessageAsync } = useSignMessage();
  const { requestChallengeAsync } = useAuthRequestChallengeEvm();
  const { push } = useRouter();

  const handleAuth = async () => {
    if (isConnected) {
      await disconnectAsync();
    }

    const { account, chain } = await connectAsync({
      connector: new MetaMaskConnector(),
    });

    const { message } = await requestChallengeAsync({
      address: account,
      chainId: chain.id,
    });
console.log(message);
    const signature = await signMessageAsync({ message });
    console.log(signature);
    // redirect user after success authentication to '/user' page
    const { url } = await signIn("moralis-auth", {
      message,
      signature,
      redirect: false,
      callbackUrl: "/user",
    });
    /**
     * instead of using signIn(..., redirect: "/user")
     * we get the url from callback and push it to the router to avoid page refreshing
     */
    push(url);
  };

  return (
    <div>
      <h3>Web3 Authentication</h3>
      <button onClick={handleAuth}>Authenticate via Metamask</button>
    </div>
  );
}

export default SignIn;
            """)

        with open('pages/user.jsx', 'w') as f:
            f.write("""
import { getSession, signOut } from "next-auth/react";
function UserPage({ user }) {
  return (
    <div>
      <h4>User session:</h4>
      <pre>{JSON.stringify(user, null, 2)}</pre>
      <button onClick={() => signOut({ redirect: "/signin" })}>Sign out</button>
    </div>
  );
}

export async function getServerSideProps(context) {
  const session = await getSession(context);

  // redirect if not authenticated
  if (!session) {
    return {
      redirect: {
        destination: "/signin",
        permanent: false,
      },
    };
  }

  return {
    props: { user: session.user },
  };
}
export default UserPage;

            """)

    def initialize_project(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.run_command('npm i ', '\n\n\nInitializing Project\n\n\n')
        print("\n\n\nProject installed....   Have a great day legend\n\n\n\n\n\n")
        print("\n\n\nEDIT .env.local AND PUT IN YOUR MORALIS CREDENTIALS FIRST\n\n\n\n(API key AND postresql credentials) `\n\n\n\n\n\n")
        print("\n\n\nEnter into the project name directory and start your project with `npm run dev`\n\n\n\n\n\n")

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        project_name = input("\n\n\n\nEnter project name in all lowercase with no extra characters: (i.e. mybadassproject) ")
        self.create_project(project_name)
        self.initialize_project()

next_js_app = NextJsApp()
next_js_app.run()
