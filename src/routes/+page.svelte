<script>
	import { onDestroy } from 'svelte';
</script>
<script lang="ts">
    import { Command } from '@tauri-apps/api/shell'
	import '$lib/app.css';
    let command;


    Command.sidecar('binaries/sod').spawn().then(cmd => {
        command = cmd;
        console.log('starting sod...');
    }).catch(error => {
        console.error('failed to start sod...', error);
    });
    
    onDestroy(() => {
        command.kill();
        console.log('killed sod...')
    });
</script>


    <!-- <div class="h-dvh flex flex-col justify-center items-center">
        <div class="flex flex-col justify-center mb-14">
            <h class="text-5xl">modworm</h>
            <h1 class="text-md text-right">soil v0.0.0</h1>
        </div>

        <form class="flex flex-col" on:submit={handleSubmit}>
            <div class="relative flex flex-row h-fit">
                <input type="text" class="bg-gray-800 p-2 mr-1 rounded-bl-xl focus:outline-none focus:ring-2 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={ip} placeholder="127.0.0.1">
                <input type="text" class="bg-gray-800 p-2 rounded-tr-xl focus:outline-none focus:ring-2 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={port} placeholder="50902"> <!-- TODO -->
                <!-- <div class="absolute -top-3 left-3 text-gray-400 text-m">IP</div>
                <div class="absolute -bottom-3 right-3 text-gray-400 text-m">port</div>
            </div>
            <button class="text-5xl p-5 text-gray-500 hover:text-white">&rarr;</button>
        </form>
    </div>
{:else}
    <SocketChecker ip={ip} port={port} />
{/if} --> -->


