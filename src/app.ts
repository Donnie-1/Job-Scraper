import createServer from "./server";

const PORT = process.env.PORT || 3000;

function startServer() {
    const app: any = createServer();
    app.listen(PORT, () => {
        console.log(`Server running on port ${PORT}`);
    });
}

startServer(); 