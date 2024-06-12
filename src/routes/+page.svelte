
<script lang="ts">
    import '$lib/app.css';
    import { onDestroy } from 'svelte';
    import { Command, Child } from '@tauri-apps/api/shell'
    import LoadingSnake from '$lib/loading_snake.svelte';
    
    // let command: Child;

    // Command.sidecar('binaries/sod').spawn().then(cmd => {
    //     command = cmd;
    //     console.log('starting sod...');
    // }).catch(error => {
    //     console.error('failed to start sod...', error);
    // });
    
    // onDestroy(() => {
    //     command.kill();
    //     console.log('killed sod...')
    // });
</script>
<div class="container mx-auto p-4">
    <div class="grid grid-flow-dense grid-cols-3">
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>        
        <div class="border row-span-3">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border row-span-2 col-span-2">
            <LoadingSnake radius={6} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
        <div class="border">
            <LoadingSnake radius={3} color={"bg-blue-600"}/>
        </div>
    </div>
</div>