/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
            protocol: 'https',
            hostname: 'thispersondoesnotexist.com',
            port: '',
            pathname: '/',
            },
    ],
    },
};

export default nextConfig;
