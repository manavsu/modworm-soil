
<script lang="ts">
  import "$lib/app.css";
  import Error from '$lib/error.svelte';
  import MapDashboard from './map_dashboard.svelte';

  import LoadingSnake from '$lib/loading_snake.svelte';
	import { error } from "@sveltejs/kit";
	import { onMount } from "svelte";
  import { CheckSocket } from "$lib/modbus_client";
	import { page } from "$app/stores";

  export let ip: string;
  export let port: string;

  let verified: boolean;


  onMount(async () => {
    verified = await CheckSocket(ip, port);
  });
  
</script>

{#if verified == null}
  <LoadingSnake />
{:else}
  {#if verified}
    <MapDashboard ip={ip} port={port}/>
  {:else}
    <Error path="/" message="unable to discover {ip} : {port}"/>
  {/if}
{/if}
