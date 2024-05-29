<script lang="ts">
	import '$lib/app.css';
	import { onMount } from 'svelte';
	import Register from './[ip]:[port]/register.svelte';
	import { ModbusDataType } from '$lib/modbus_data_type';
	import { ReadRegisters } from '$lib/modbus_client';
	import type { RegisterStore } from '$lib/register_store';
    import LoadingSnake from '$lib/loading_snake.svelte';

    let ip: string = "";
    let port: string = ""; // TODO

    function handleSubmit() {
        ip = ip || "127.0.0.1";
        port = port || "50902";
    }

</script>

<div class="h-dvh flex flex-col justify-center items-center">
    <div class="flex flex-col justify-center mb-14">
        <h class="text-5xl">modworm</h>
        <h1 class="text-md text-right">soil v0.0.0</h1>
    </div>

    <form class="flex flex-col" action="/{ip}:{port}" on:submit={handleSubmit}>
        <div class="relative flex flex-row h-fit">
            <input type="text" class="bg-gray-800 p-2 mr-1 rounded-bl-xl focus:outline-none focus:ring-2 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={ip} placeholder="127.0.0.1">
            <input type="text" class="bg-gray-800 p-2 rounded-tr-xl focus:outline-none focus:ring-2 focus:ring-gray-700 hover:ring-2 hover:ring-gray-800" bind:value={port} placeholder="50902"> <!-- TODO -->
            <div class="absolute -top-3 left-3 text-gray-400 text-m">IP</div>
            <div class="absolute -bottom-3 right-3 text-gray-400 text-m">port</div>
        </div>
        <button class="text-5xl p-5 text-gray-500 hover:text-white">&rarr;</button>
    </form>
</div>
