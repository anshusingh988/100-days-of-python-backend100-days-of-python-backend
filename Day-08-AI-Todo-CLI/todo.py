import click
from rich.console import Console
from rich.table import Table
import database
import ai_service

console = Console()

@click.group()
def cli():
    """AI-Powered CLI To-Do List"""
    pass

@cli.command()
@click.argument('title')
def add(title):
    """Add a new task with AI analysis."""
    database.init_db()
    with console.status("[bold green]Analyzing task with AI..."):
        analysis = ai_service.analyze_task(title)
    
    task_id = database.add_task(title, category=analysis.get('category', 'Uncategorized'), priority=analysis.get('priority', 'Medium'))
    console.print(f"[bold green]? Added task #{task_id}:[/bold green] {title} (Category: {analysis.get('category')}, Priority: {analysis.get('priority')})")
    
    subtasks = analysis.get('subtasks', [])
    if subtasks:
        console.print(f"[cyan]AI suggested {len(subtasks)} subtasks:[/cyan]")
        for sub in subtasks:
            sub_id = database.add_task(sub, category=analysis.get('category'), priority=analysis.get('priority'), parent_id=task_id)
            console.print(f"  [dim]- #{sub_id}: {sub}[/dim]")

@cli.command()
def list():
    """List all pending tasks."""
    database.init_db()
    tasks = database.get_tasks()
    
    table = Table(title="To-Do List")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Category", style="green")
    table.add_column("Priority", style="yellow")
    table.add_column("Status", style="red")
    
    for row in tasks:
        id, title, category, priority, status, parent_id = row
        title_display = title if not parent_id else f"  ? {title}"
        table.add_row(str(id), title_display, category, priority, status)
        
    console.print(table)

@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    """Mark a task as completed."""
    database.init_db()
    database.complete_task(task_id)
    console.print(f"[bold green]? Task #{task_id} marked as completed![/bold green]")

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task and its subtasks."""
    database.init_db()
    database.delete_task(task_id)
    console.print(f"[bold red]? Task #{task_id} and its subtasks deleted![/bold red]")

if __name__ == '__main__':
    cli()
