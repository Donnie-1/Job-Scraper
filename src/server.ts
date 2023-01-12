import express, {Application, Request, Response} from 'express';
import { TodoModel } from './todo.schema';


export default function createServer() {
  const app: Application = express();
  app.use(express.json());

  app.get('/todos', async (req: Request, res: Response) => {
      const todos = await TodoModel.find();
      res.send(todos);
  });

  app.post('/todos', async (req: Request, res: Response) => {
      const todo = new TodoModel(req.body);
      await todo.save();
      res.send(todo);
  });

  app.put('/todos/:id', async (req: Request, res: Response) => {
      const todo = await TodoModel.findByIdAndUpdate(req.params.id, req.body, { new: true });
      res.send(todo);
  });

  app.delete('/todos/:id', async (req: Request, res: Response) => {
    await TodoModel.findByIdAndDelete(req.params.id);
    res.send({ message: 'Todo deleted' });
  });
}