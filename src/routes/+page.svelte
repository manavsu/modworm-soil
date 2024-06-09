
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

<LoadingSnake radius={8}/>


