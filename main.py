import click
from rich.console import Console
from rich.table import Table
from database import init_db, add_task, get_tasks, complete_task, delete_task
from ai_service import analyze_task

console = Console()

@click.group()
def cli():
    """AI-Powered CLI To-Do List"""
    init_db()

# 🔹 Add Task
@cli.command()
@click.argument('title')
def add(title):
    with console.status("[bold green]Analyzing task with AI..."):
        ai_result = analyze_task(title)
        category = ai_result.get('category', 'General')
        priority = ai_result.get('priority', 'Medium')

    task_id = add_task(title, category, priority)

    console.print(f"[bold green]✓ Added Task #{task_id}[/bold green]")
    console.print(f"{title} [cyan]({category} | {priority})[/cyan]")

    # Subtasks
    subtasks = ai_result.get('subtasks', [])
    if subtasks:
        console.print("\n[yellow]Generated Subtasks:[/yellow]")
        for sub in subtasks:
            sub_id = add_task(sub, category, priority, parent_id=task_id)
            console.print(f"  ↳ {sub} (#{sub_id})")

# 🔹 List Tasks
@cli.command()
def list():
    tasks = get_tasks()

    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="🚀 AI To-Do List")

    table.add_column("ID", style="cyan")
    table.add_column("Task", style="magenta")
    table.add_column("Category", style="blue")
    table.add_column("Priority", style="yellow")
    table.add_column("Status", style="green")

    for t in tasks:
        t_id, title, category, priority, status, parent_id = t
        display_title = title if not parent_id else f"  ↳ {title}"

        table.add_row(str(t_id), display_title, category, priority, status)

    console.print(table)

# 🔹 Mark Done
@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    complete_task(task_id)
    console.print(f"[green]Task #{task_id} completed![/green]")

# 🔹 Delete Task
@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    delete_task(task_id)
    console.print(f"[red]Task #{task_id} deleted![/red]")

# 🔹 AI Suggestions
@cli.command()
@click.argument('goal')
def suggest(goal):
    suggestions = [
        f"Break '{goal}' into smaller tasks",
        f"Set a deadline",
        f"Start with easiest part",
        f"Use Pomodoro (25 min focus)",
        f"Avoid distractions"
    ]

    console.print("[bold cyan]💡 AI Suggestions:[/bold cyan]")
    for s in suggestions:
        console.print(f"- {s}")

# 🔹 Stats
@cli.command()
def stats():
    tasks = get_tasks()

    total = len(tasks)
    completed = sum(1 for t in tasks if t[4] == "Completed")
    pending = total - completed

    console.print(f"[green]Total:[/green] {total}")
    console.print(f"[blue]Completed:[/blue] {completed}")
    console.print(f"[red]Pending:[/red] {pending}")

if __name__ == '__main__':
    cli()