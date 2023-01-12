import * as mongoose from 'mongoose';
import { Todo } from './interface';

const TodoSchema = new mongoose.Schema({
    id: {
        type: String,
        required: true
    },
    title: {
        type: String,
        required: true
    },
    description: {
        type: String,
        default: ''
    },
    dueDate: {
        type: Date,
        default: null
    },
    completed: {
        type: Boolean,
        default: false
    },
    user: {
        type: String,
        required: true
    }
});
export const TodoModel = mongoose.model<Todo & mongoose.Document>('Todo', TodoSchema);
