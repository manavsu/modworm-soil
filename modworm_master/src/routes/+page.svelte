<script lang="ts">
    import "../app.css";
    import { onMount } from 'svelte';
    import Register from "./register.svelte";
    import { ModbusDataType } from "$lib/modbus_data_type";
    import { ReadRegisters } from "$lib/modbus_client";
    import type { RegisterStore } from "$lib/register_store";
    
    export let ip:string = "127.0.0.1";
    export let port:number = 5002;
    export let func_code:number = 4;
    export let address:number = 0;
    export let count:number = 100;

    let registers: Array<RegisterStore> = [];

    let intervalId: number;
    onMount(() => {
        intervalId = setInterval(async () => {
            try {
                const result = await ReadRegisters(ip, port,func_code, address, count);
                for (let i = 0; i < count; i++) {
                    registers[i] = {address: address + i, value: result[i], type: ModbusDataType.UInt16};
                }
                registers = [...registers];
            } catch (error) {
                console.error(error);
            }
        }, 1000);

        return () => {
            clearInterval(intervalId);
        };
    });

</script>

<style lang="postcss">
    :global(html) {
        background-color: theme(colors.gray.950);
    }
    .grid-col-fill {
        grid-template-columns: repeat(auto-fill, minmax(104px, 1fr));
    }
</style>

<div class="grid grid-col-fill justify-items-center bg-gray-950 text-white">
    {#each registers as reg, _}
        <Register address={reg.address} value={reg.value} type={reg.type}/>
    {/each}
</div>